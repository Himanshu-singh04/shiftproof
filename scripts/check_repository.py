"""Check tracked text formatting and relative Markdown file links without dependencies."""
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


def main():
    root = Path(__file__).resolve().parents[1]
    paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    errors = []
    for name in filter(None, paths):
        path = root / name
        if path.suffix not in {".md", ".yml", ".yaml", ".py"} and path.name not in {"CODEOWNERS", ".gitignore"}:
            continue
        text = path.read_text()
        if text and not text.endswith("\n"):
            errors.append(f"{name}: missing final newline")
        for number, line in enumerate(text.splitlines(), 1):
            if line != line.rstrip():
                errors.append(f"{name}:{number}: trailing whitespace")
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                linked = root / unquote(url.path.lstrip("/")) if url.path.startswith("/") else path.parent / unquote(url.path)
                if not linked.exists():
                    errors.append(f"{name}: missing linked file {target}")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Tracked text formatting and relative Markdown file links passed (anchors/external URLs not checked).")


if __name__ == "__main__":
    main()
