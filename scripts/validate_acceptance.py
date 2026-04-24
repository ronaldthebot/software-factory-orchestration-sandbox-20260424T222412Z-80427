from pathlib import Path
import re
import subprocess
branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
match = re.search(r"issue-(\d+)-", branch)
if not match:
    raise SystemExit(f"cannot infer issue number from branch {branch}")
issue = int(match.group(1))
root = Path.cwd()
feature = root / "features" / f"issue_{issue}.txt"
app = root / "src" / "sandbox_app.py"
if not feature.exists():
    raise SystemExit(f"missing {feature}")
if f"accepted live sandbox issue {issue}" not in feature.read_text(encoding="utf-8"):
    raise SystemExit("feature acceptance marker missing")
if f"IMPLEMENTED_ISSUES.append({issue})" not in app.read_text(encoding="utf-8"):
    raise SystemExit("sandbox app marker missing")
print(f"validated live issue {issue} on {branch}")
