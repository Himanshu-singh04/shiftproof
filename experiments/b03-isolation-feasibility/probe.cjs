'use strict';

// Reviewed synthetic probes only. Every path, listener and child belongs to B03.
const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');
const [action, inside, outside, tcpPort, udpPort, token] = process.argv.slice(2);
const report = (value) => console.log(JSON.stringify(value));
const denied = new Set(['EACCES', 'EPERM', 'ERR_ACCESS_DENIED']);
const fail = (error) => report({ action, outcome: denied.has(error.code) ? 'denied' : 'error',
  code: error.code || error.name });
const childArgs = [__filename, 'owned-child', inside, outside, tcpPort, udpPort, token];

async function probe() {
  switch (action) {
    case 'startup': return 'ready';
    case 'inside-read': return fs.readFileSync(path.join(inside, 'sentinel'), 'utf8') === 'B03_SENTINEL';
    case 'inside-write': fs.writeFileSync(path.join(inside, 'written'), 'B03_WRITE'); return true;
    case 'outside-read': return fs.readFileSync(path.join(outside, 'sentinel'), 'utf8') === 'B03_SENTINEL';
    case 'outside-write': fs.writeFileSync(path.join(outside, 'written'), 'B03_WRITE'); return true;
    case 'outside-list': return fs.readdirSync(outside).includes('sentinel');
    case 'parent-traversal': return fs.readFileSync(`${inside}/../outside/sentinel`, 'utf8') === 'B03_SENTINEL';
    case 'symlink-read': return fs.readFileSync(path.join(inside, 'escape', 'sentinel'), 'utf8') === 'B03_SENTINEL';
    case 'symlink-write': fs.writeFileSync(path.join(inside, 'escape', 'link-written'), 'B03_WRITE'); return true;
    case 'async-read': return (await fs.promises.readFile(path.join(outside, 'sentinel'), 'utf8')) === 'B03_SENTINEL';
    case 'spawn': {
      const result = cp.spawnSync(process.execPath, ['-e', 'process.stdout.write("B03_CHILD")'], {
        env: {}, encoding: 'utf8', timeout: 1000, maxBuffer: 1024,
      });
      if (result.error) throw result.error;
      if (result.status !== 0 || result.stdout !== 'B03_CHILD') throw new Error('child-control-failed');
      return true;
    }
    case 'exec':
      // Replace this owned process only; the command contains no interpolated input.
      process.execve('/bin/sh', ['/bin/sh', '-c', 'printf B03_EXEC'], {});
      throw new Error('exec-returned');
    case 'tcp': return await new Promise((resolve, reject) => {
      const socket = require('node:net').connect({ host: '127.0.0.1', port: Number(tcpPort) });
      socket.setTimeout(700, () => socket.destroy(new Error('local-timeout')));
      socket.on('error', reject);
      socket.on('connect', () => socket.write(`GET /${token} HTTP/1.0\r\n\r\n`));
      let response = '';
      socket.on('data', (data) => { response += data; });
      socket.on('end', () => resolve(response.endsWith(token)));
    });
    case 'http': return await new Promise((resolve, reject) => {
      const request = require('node:http').get({ host: '127.0.0.1', port: Number(tcpPort),
        path: `/${token}`, agent: false }, (response) => {
        let body = '';
        response.on('data', (data) => { body += data; });
        response.on('end', () => resolve(response.statusCode === 200 && body === token));
      });
      request.setTimeout(700, () => request.destroy(new Error('local-timeout')));
      request.on('error', reject);
    });
    case 'udp': return await new Promise((resolve, reject) => {
      const socket = require('node:dgram').createSocket('udp4');
      const timer = setTimeout(() => { socket.close(); reject(new Error('local-timeout')); }, 700);
      socket.on('error', (error) => { clearTimeout(timer); socket.close(); reject(error); });
      socket.on('message', (message) => { clearTimeout(timer); socket.close(); resolve(message.toString() === token); });
      socket.send(token, Number(udpPort), '127.0.0.1', (error) => {
        if (error) { clearTimeout(timer); socket.close(); reject(error); }
      });
    });
    case 'environment': return { removed: !Object.hasOwn(process.env, 'B03_SYNTHETIC_SECRET'),
      kept: process.env.B03_KEEP === 'B03_PUBLIC' };
    case 'output': process.stdout.write('X'.repeat(128 * 1024)); return true;
    case 'wait': await new Promise((resolve) => setTimeout(resolve, 2500)); return true;
    case 'owned-child':
      // One bounded, low-CPU child; self-expiry is an independent cleanup backstop.
      await new Promise((resolve) => setTimeout(resolve, 3000)); return true;
    case 'parent-failure':
    case 'detach-failure':
    case 'detach-wait': {
      const child = cp.spawn(process.execPath, childArgs, {
        detached: action.startsWith('detach'), stdio: 'ignore', env: {},
      });
      child.on('error', (error) => { fail(error); process.exit(0); });
      child.on('spawn', () => {
        report({ action, outcome: 'allowed', pid: child.pid, token });
        child.unref();
        if (action !== 'detach-wait') process.exit(23); // Deliberate parent failure.
      });
      if (action === 'detach-wait') await new Promise((resolve) => setTimeout(resolve, 2500));
      return 'parent';
    }
    default: throw new Error('unknown-probe');
  }
}

probe().then((value) => {
  if (value !== 'parent') report({ action, outcome: 'allowed', value });
}).catch(fail);
