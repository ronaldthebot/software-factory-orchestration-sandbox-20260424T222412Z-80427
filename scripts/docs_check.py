from pathlib import Path
if "Live Sandbox" not in Path("README.md").read_text(encoding="utf-8"):
    raise SystemExit("README marker missing")
print("docs endgame passed")
