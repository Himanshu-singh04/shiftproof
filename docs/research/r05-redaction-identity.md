# R05: truthful identity after redaction

Status: **retain truthful domains; refuse unrepresentable identity**, for
[issue #25](https://github.com/Himanshu-singh04/shiftproof/issues/25).
Documentation/public-source work only; no identity policy or schema adopted.

## Authority and bound

Founder authorized ongoing business/development research while ReleaseLens is prioritized.
The R05 task message dispatches this distinct identity question under that mandate to
the same persistent GPT-6 Astra / OpenCode worker; no subagents or permission changes.
Successful start **2026-11-20 06:44:30 UTC**; deadline **08:44:30 UTC**, earlier if enough.
One 180–250-line note, at most four primary external documents and eight paper cases.
Approved main: `04c25991698612b9aabe8e2d1bfaee58bf9fb7a8`.

Preserve these founder-unapproved branches/checkouts/PRs at exact revisions:
- B03a #16: `644be51bbbac996f7fc9023530516bf37a409190`; full source/acceptance audit pending.
- R01 #18: `0de10807e8a02c918e19f6ee6c0f7a0320158d39`.
- R02 #20: `6dd79d5b9714eddfcfc3985aa50518055fecb8e5`.
- R03 #22: `8ac7ae8f2007d729d60aac443a2b9df6e6acf204`.
- R04 #24: `4a2c280d3848aa5389ffb452f13fb8ea6000f485`; independent A1–A6 audit passed.

## A1: contract map and terms

References use approved-main line numbers: [evidence contract](../evidence-contract.md)
(EC), [operations](../operations.md) (OP), [testing](../testing.md) (T). These specify
intended behavior; there is no implemented schema, intake or publisher to validate.
**Original** means the selected bytes before redaction; **retained** means the bytes
actually kept for review. An excerpt is only a selection; a redacted derivative may
change bytes inside that selection. Neither becomes the original by being hashed.

| Clauses | Current obligation / unresolved boundary |
| --- | --- |
| EC L18–35 | Unique IDs, UTF-8 strings, explicit repository-snapshot versus run-bundle bases, contained references; one-based source lines/columns with exclusive ends. A locator into the original is not a locator into a rewritten copy. Column encoding details beyond that are unspecified. |
| EC L36–51 | Required lists/fields, closed enums, `null` plus gap for unknowns; SHA-256 references include lowercase digest and byte size. Hashes detect changes relative to a reference, not author/publisher authenticity. Generic null language does not settle each required hash field's admissible shape. |
| EC L55–69 | Exact versions, locks with format/workspace/resolution, actual artifact identity/hash, dirty repository file-content manifest; commit SHA alone insufficient. No redacted-lock or sanitized-artifact identity variant is defined. Archive versus installed-tree serialization needs a precise domain. |
| EC L80–100 | Citation contentHash, locator, applicability, publisher/date and permitted excerpt or snapshot; URL alone insufficient, retention restrictions recorded. Which bytes contentHash covers when only an excerpt is kept is not specified. Links do not authenticate; no auto-fetch on viewing. |
| EC L104–109 | Callsite fileHash/range and ID derived from file hash/range/symbol; minimal excerpts, sensitive literals redacted before persistence. Original file hash versus safe excerpt integrity are different assertions. No source-map or redacted-file identity field is defined. |
| EC L139–153 | Observation rawHash, redactedArtifact, normalizedHash, typed capture and gaps; redact raw artifacts before persistence, lost required dimension => unknown, no published hashes of secrets. Raw/normalized hash domains relative to redaction and serialization are not fully specified. |
| EC L164–180, L241–288 | Normalization is declared/ordered, cannot erase material differences; Comparison owns outcomes, absent evidence cannot pass. Redaction is not an automatically approved normalization. Malformed identity cannot be repaired by setting status unknown. |
| EC L340–367 | Validated JSON/inert rendering, marker last, hash/reference checks, whole-record canonical semantic projection with only listed exclusions. Artifact-byte verification and semantic-digest verification are separate. Normalization does not remove raw capture hashes from the digest. |
| OP L63–65, L77–92, L98–114; T01/T06/T08/T10/T11 | Complete unknown exits 2; invalid/failed/incomplete exits 3. Publication safety is independent; logs redacted, operator reviews sharing, local retention is not encryption/backup assurance. Missing/corrupt artifacts rejected; no secret payload/hash leakage or false authentication. |

**Three different questions:** does this digest bind the asserted byte sequence; does
this reader possess that sequence and verify it; and did it come from the claimed
source? A matching retained-byte digest answers neither original-byte identity nor
authenticity. A publisher name, path, timestamp or reviewer assertion is not a signature.
Hashes and sizes identify a chosen encoding, not merely equivalent parsed values:
whitespace/newlines, archive encoding or serialization changes can change byte identity.
The sorted repository manifest and typed capture encodings need exact specifications;
R05 does not supply one or import RunRecord canonicalization into every hash field.

**Null is an unresolved type question, not a workaround.** EC L36 permits unknown
values with gaps, while L47 describes hash objects and L104–107 explicitly mark only
resolvedSymbol/resolutionPath nullable. L139–153 names required capture hash fields
without a redaction-specific null rule. This tension needs field-level clarification.
Do not assert either a universal nullable-hash schema or an already adopted prohibition
on all null hashes. Pending that decision, a producer cannot call an unvalidated null,
omitted required field, empty-string digest or invented placeholder hash a valid record.
EC L51 diagnostic unknown is not evidence that a complete RunRecord can be constructed.

## Supporting primary sources: three, read 2026-11-20

Repository clauses control the decision. These documents support narrow distinctions;
no HTTP field, annotation model or password-storage mechanism is adopted by ShiftProof.

| ID / primary document | Locator, supported claim and limit |
| --- | --- |
| P1 [IETF RFC 9530: Digest Fields](https://www.rfc-editor.org/rfc/rfc9530.txt), February 2024 | Sections 1.2, 2–3 distinguish conveyed content from entire selected representation; B.3 illustrates partial content. Sections 1.2/6.1 say digests alone provide no authentication/privacy or general malicious-tampering protection; 6.5 limits at-rest verification without persisted encoded content. This motivates naming byte domains, not adoption of HTTP semantics for EC. |
| P2 [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | “Introduction” and “When Password Hashes Can Be Cracked”: candidates can be hashed and compared; fast SHA-256 enables rapid guessing of weak passwords. This supports a disclosure concern for predictable secret-bearing inputs, not a claim every source digest reveals a high-entropy secret or permission to publish one. No password algorithm/salt/pepper recommendation imported. |
| P3 [W3C Web Annotation Data Model](https://www.w3.org/TR/2017/REC-annotation-model-20170223/), 23 February 2017 | Sections 4.2.4–4.2.6 distinguish copied/normalized text, text positions and byte positions; text positions are brittle under edits, copying quotes has retention concerns. Section 4.3 associates selection with a representation state. Its zero-based selectors/normalization are not EC's one-based source-range rules. |

Response SHA-256 values (P1 raw text; P2/P3 HTML, not rendered Markdown):

```text
P1 544dbb7d9afceafa8c9931d9924ca6cff2b4807274166d7ed2483342ef2cdd6a
P2 9fdf8b41477e641594832cebd4dbb388d8d61ebe71c7d3a4bdec21d235fc8556
P3 a7513e022f56c0a6f4e99ac11aec03f3451d1ff1ce14054780b3ccfb38fa7980
```

Only public-document responses were hashed, not invented secrets or paper-case inputs.
P2 is a mutable page; its digest records this retrieval. No linked sources were followed.
The W3C selector sections were read directly from the public response after a managed
tool-output search was denied by external-directory permissions; no denied file content
was returned or permissions changed. This was a tool-path denial, not a provider error.

## A2: identity and retention matrix

All rows assume safe read-only acquisition and a frozen input generation. Neither is
proved by a digest. “Retain” below means permissible product evidence, not authority to
copy secret-bearing originals into scratch/cache/logs or erase the operator's source.
Local operator possession does not itself make publication of a secret-derived hash safe.

| Record / asserted hash domain | Permissible retained bytes / locator | Reader capability, disclosure risk and residual gap |
| --- | --- | --- |
| Repository file / Callsite: selected original file bytes for fileHash; repository manifest binds sorted file-content entries | Minimal safe excerpt; original snapshot remains the separate declared source base. Range belongs to the original file, not the excerpt's line numbers. A redacted file is not a byte-identical snapshot. | With lawful safe access to the original, verify original file/manifest and range; excerpt alone cannot. Secret-bearing originals raise L153/T10 concerns even if only the digest is shared. Missing/unsafe original identity is not cured by hashing sanitized text; field/null representation unresolved. |
| Source/target lock: selected original lock content, plus format/workspace/resolution | Safe original lock only where retention is permitted; removing embedded credentials makes a different file. Package-resolution identity must remain exact, not inferred solely from unchanged version labels. | Reader can verify complete supplied lock bytes, not reconstruct deleted credentials from redacted bytes. Original hash can act as a guess/equality check; sanitized hash cannot attest original lock. OP L98 preflight failure applies if truthful identity is unavailable. |
| Source/target package artifact: actual selected artifact, distinct from lock/registry metadata | Reviewed safe artifact or reference under explicit provisioning base; precise archive/tree byte domain still needed. Editing a package to remove content changes the artifact. | Complete same-domain bytes permit a relative hash check; lock integrity metadata alone does not verify installed content or publisher authenticity. Missing artifact unsupported under EC L66–69; a sanitized package cannot keep original artifact identity. |
| Document Citation: contentHash of an identified representation, but full-source versus excerpt domain is ambiguous | Allowable excerpt or local snapshot with locator/version/date/publisher and retention restrictions. Original heading/line locator remains original; any local excerpt position is separate descriptive context, not an invented schema field. | Full retained safe source can support full-source verification; excerpt supports only its own bytes/text and limited claim inspection. Full-source digest cannot be recomputed from an excerpt; excerpt digest cannot silently stand for full source. Secret, licensing, missing-context and version uncertainty remain gaps. |
| Observation capture: rawHash and normalizedHash; pre/post-redaction order and typed byte serialization unresolved | Only redacted raw/normalized views may persist, with preserved type/order distinctions and declared normalization rules. redactedArtifact is a bundle-relative reference, not proof of what rawHash means. | Reader checks retained bytes only against a matching specified domain. Deleted values cannot be reconstructed or compared; REDACTION_LOSS required if a dimension is lost. Pre-redaction secret hash is prohibited; post-redaction hash relabelled original is false. Truthful field representation remains a gate. |

The completion manifest binds the actual referenced artifact bytes, while semanticDigest
binds the EC L350–367 projection of a valid RunRecord. Neither can substitute for a
missing fileHash, lock hash, citation domain or rawHash. A sanitized JSON record can be
internally self-consistent yet misstate all those identities. Rehashing a container of
secret-derived hashes does not establish that its contents are safe to publish. Moving
such values into operationalMetadata is also forbidden by EC L358–359.

The secret-hash prohibition is explicit; the treatment of a whole source/lock digest
containing both public context and a secret is not separately spelled out. If context
is known and the remaining value is guessable, the whole-file digest can test guesses
just as a direct digest can. No entropy threshold or automatic safe-hash exception is
approved. Recommend treating unresolved disclosure risk as a refusal condition, not
assuming a whole-file hash is harmless because it is not labelled a password hash.
Length-preserving masks can still disclose lengths and do not restore original byte
identity. Source names, URLs, locator context and diagnostic details also need review.

## A3: three dispositions, with distinct validity and exit consequences

| Disposition | Conditions / allowed claim | Boundary and trade-off |
| --- | --- | --- |
| D1 Preserve a safe original identity | Original bytes/domain are unambiguous, permitted and available to the required reader; hashes/ranges refer to those bytes. Display may omit irrelevant safe text without replacing the identified source. | Reader may claim relative byte verification and inspect selected evidence, never authenticity or whole-source verification from an excerpt alone. Applicable only where privacy/retention permit; no redacted original is relabelled byte-identical. |
| D2 Retain honest unknown in a structurally valid record | Required identities remain truthful and safe; missing semantic evidence uses existing nullable references/gaps and complete coverage/closure. Example: safe fileHash with unresolvedSymbol null, mapping gap; replay never run, legitimate empty observation list and NOT_RUN/ISOLATION_UNAVAILABLE. | Complete unknown could exit 2 only after independently safe publication. No deleted collected observation, fabricated hash, new nullability or hidden exclusion. REDACTION_LOSS is necessary for lost dimensions but is not alone proof that all required hash fields are valid. |
| D3 Refuse the evidence publication | Required original identity is unsafe/unavailable, domain ambiguous, required reference cannot validate or a necessary field lacks a justified representation. Stop with redacted diagnostic; do not emit a complete bundle asserting that identity. | Existing invalid-input/failed/incomplete exit 3, no completion marker. Loses deliverable coverage but preserves truth/privacy. A separately approved contract clarification is needed before claiming a broader representation; no new “redacted-only” mode is adopted. |

For **invalid record/identity**, unknown is a diagnostic rather than valid completion
(EC L50–51, L245–246). For **incomplete execution**, state is pending/running/failed/
cancelled with gaps and exit 3; an already validated incompatibility may remain, but
does not turn the run complete. For **publication refusal**, even structurally valid
unknown evidence cannot authorize an unsafe publisher (OP L77–85). For **complete
unknown**, all required structure/identity/closure still holds; absence of replay is
not a pass. Aggregate precedence still permits a validated fail to outrank unknowns;
the paper cases here contain no such fail and claim no executed observation.

The hard conflict is not solved by choosing a stronger hash: the reader needs the
asserted original bytes for original verification, persistence must exclude sensitive
literals, hashes of secrets cannot be published, and required fields cannot be omitted
or silently changed to mean sanitized bytes. If originals are unsafe to identify and
only a derivative remains, these obligations may have no established joint encoding.
D3 is the conservative recommendation until a truthful current-contract representation
is demonstrated. D2 is available for semantic uncertainty, not a schema escape hatch.
No encryption, salt/HMAC, signatures, storage service or trusted upload is presumed.

## A4: eight paper cases, no execution or invented digest values

Each changed case uses C1's stable no-secret control for the relevant record type.
These are proposed validation/claim oracles, not approved fixtures or measured results.
Any conditional exit 2 presumes safe acquisition/publication; the current publication
blocker means none of these cases authorizes producing a completed artifact now.

| Case / control and change | Actually verifiable / reader claim | Disposition and remaining uncertainty |
| --- | --- | --- |
| C1: safe unchanged source/lock/artifact/doc and declared capture-byte domain, exact versions, original bytes available | Verify the exact byte domain and valid original ranges against supplied bytes; inspect allowed excerpts. Claim “matches this reference”, not “authentic publisher” or “SDK compatible”. | D1; missing replay keeps outcomes unknown under D2. Complete unknown/exit 2 only conditionally; no claim of an actual capture or resolved capture-domain policy. |
| C2: replace a secret literal and remove a newline before a callsite, unlike C1's unchanged safe source | Reader can inspect sanitized text; original range now selects different text in the derivative. Original range cannot be translated by reusing its numbers; even preserved columns do not prove original equality. | No sanitized digest in fileHash with original provenance. REDACTION_LOSS/mapping uncertainty as relevant; D3 if original file identity is unsafe or unrepresentable. No new source-map/nullable-range exception. |
| C3: redact an embedded credential from the selected lock; same safe-version control in C1 | Sanitized lock bytes/remaining package labels can be checked, not the original lock's full byte identity or complete resolution provenance. Publishing original digest may disclose a guess test. | D3/exit 3 if original safe identity unavailable; OP L98 explicit correction/new run, never latest resolution or same-run relabelling. No implied credential-safe canonical lock hash. |
| C4: retain only a permitted doc excerpt while recording a whole-source digest, versus C1 full safe source | Reader checks excerpt text and locator plausibility, cannot recompute whole-source hash. Substituting an excerpt digest changes the asserted domain; exact SDK applicability still needs evidence. | EC L83 allows excerpts, so do not ban them categorically. Full-source verification claim refused; missing required citation evidence stays unknown where validly represented (D2), otherwise D3 until contentHash domain/reader policy is clarified. |
| C5: two distinct originals become identical after redaction, versus repeated identical C1 original | Same sanitized bytes necessarily yield the same sanitized digest; this is information loss before hashing, not evidence of a cryptographic collision. Reader cannot distinguish the deleted values or infer original equality. | Never merge original identities/observations or declare equivalence from the sanitized match. D2 only with safe distinct original identities and valid loss gaps; otherwise D3. Required comparison dimension remains unknown. |
| C6: original snapshot/lock/artifact bytes unavailable to reader, versus C1 retained originals | Stored digest alone cannot be recomputed; present derivative is a different domain. Permitted excerpt-only docs follow C4, not a blanket original-file substitute. | Missing referenced source/artifact => reject completed display under EC L347–348/OP L103. D3 for unverifiable required identity; valid missing-evidence diagnostic only, no silent refetch/fabricated null hash. Prior claimed origin remains unverified. |
| C7: redaction removes a required captured comparison value, versus C1 safe retained value | Reader can inspect remaining redacted/normalized bytes only; cannot establish equivalence or difference on the missing dimension. A normalized digest cannot restore raw evidence. | EC L152–153 mandates unknown/REDACTION_LOSS. D2 only if a valid truthful capture-hash representation exists; rawHash domain/nullability unresolved => D3, not automatic omission of the collected observation. Replay is not executed here. |
| C8: change retained artifact or original source after review, versus C1 stable bytes; alternatively change bytes and recorded hashes together | Old reference mismatch rejects altered bytes; recomputing supplied hashes may yield internal consistency but no evidence of the earlier reviewed revision. Changes to the semantic projection affect semanticDigest; byte-only formatting can leave that projection unchanged while artifact hash changes. | Reader rejects stale/missing-reference bundle, failed validation exit 3. New evidence requires new identity/run and review, never status repair or treating a rewritten reference as approval. No signature/authenticated-review guarantee claimed. |

Cases do not erase failed/scanned counts, change scope after comparison or remove
required closure IDs to make a report validate. Existing Gap detail/requiredEvidence/
nextAction may describe loss safely; they cannot smuggle a second undocumented hash
domain, secret value or alternate identity into prose and treat it as schema support.

## A5: smallest clarification and distinct later question

Recommend one **rawHash/redactedArtifact domain-and-refusal clarification** at EC
L139–153, reconciled with L36–37/L47 (unknown/hash shape), L179 (retained views) and
L347–367 (reader/digest). Preserve the secret-hash prohibition. Where no safe truthful
required domain can be supplied and verified as required, specify refusal rather than
silently substituting sanitized bytes or assuming nullability. Related source/lock/doc
ambiguities in the matrix remain undecided; this is not a whole-schema redesign or a
change to existing clauses, fields or statuses.

Smallest concrete decision within that rule: settle **rawHash versus redactedArtifact**
under EC L139–153. If rawHash means pre-redaction capture, publishing a secret-derived
hash conflicts with L153; if it means retained redacted capture, the exact serialization
and inability to recover removed observations must be explicit. Confirm how generic
null/gap handling applies before allowing any nullable hash. If neither interpretation
is acceptable under current fields, refuse the record and return a separate revision
request. Avoid promising original reproducibility from only sanitized content.

Trade-off: retaining original identity improves exact comparison/reproduction only
where those bytes and hashes are safe; retained-only identity narrows what a reader can
verify and may require a separately approved contract change. Refusal reduces useful
coverage but avoids an apparently complete evidence chain with a false original claim.
Confidence high in the byte-domain/information-loss distinction; field-specific valid
encodings and sufficient redaction policy remain unknown. An approved precise domain/
nullability interpretation plus independently checked cases could reduce that uncertainty;
a successful digest match alone could not. No new paid spend or estimated timings.

Ranked distinct later question: **what minimum excerpt/context and retention rights let
a reviewer check a version-specific citation claim without the full document?** Require
the hash-domain decision first, exact version/locator rules and explicit permitted
retention. Stop where omitted context changes the claim, rights prevent needed evidence
or a new field/status/storage service would be required; return unknown/refusal, not
automatic retrieval or a synthetic assertion of publisher trust.

Operators must review secrets, metadata and sharing, retain permitted reproducible
bytes and keep access to the declared source base. Maintenance includes redaction
rules, typed serialization, range/version drift, closure validation and retention changes.
Neither a secret scanner nor manual approval proves absence of all sensitive content;
burden, coverage and customer decision value remain unmeasured. No static-only scope
adoption, implementation, fixture, probe, install, customer input/outreach or safe-intake
claim follows. Acquisition/immutability, publisher composition and replay isolation are
independent open gates; the exhausted publication API frontier is not reopened here.

## A6: provenance and delivery limits

R04's [reviewed exact note](https://github.com/Himanshu-singh04/shiftproof/blob/4a2c280d3848aa5389ffb452f13fb8ea6000f485/docs/research/r04-publication-transaction.md)
is provisional context only; its commit-boundary interpretation remains undecided.
Publication stays blocked and replay **disabled / unknown / ISOLATION_UNAVAILABLE**.
ReleaseLens #17 merged; N1–N4 apply there only. Its synthetic scope/sequence and docs
reconciliation are the sole pending founder decision; no PR approval is active.
Authority is the existing founder mandate and this task dispatch. A generated summary
or synthetic continuation is context, not a new human approval or evidence of customer
participation. No provider interruption or synthetic recovery occurred in this round
as of this note; any later event must retain its actual provenance in the PR record.
Provider/quota error stops without retry/bypass. Required checks, exact head/base,
failure history and literal Sourcery are in the PR handoff. Existing 56 files, 55 SDD
headings and five predecessor refs/checkouts remain preserved; no self-dispatch.
