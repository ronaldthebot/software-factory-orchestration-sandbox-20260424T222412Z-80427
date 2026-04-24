from pathlib import Path
for path in Path.cwd().rglob("*"):
    if path.is_file() and ".git" not in path.parts:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "ghp_" in text or "gho_" in text or "github_pat_" in text:
            raise SystemExit(f"credential-like token found in {path}")
print("security endgame passed: no credential-like tokens in worktree files")
