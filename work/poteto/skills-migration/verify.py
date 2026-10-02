import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[3]
manifest = json.loads((Path(__file__).parent / "manifest.json").read_text())
errors = []

for category in ("files", "preserved"):
    for name, expected in manifest[category].items():
        path = root / name
        if not path.is_file():
            errors.append(f"missing {category} file: {name}")
            continue
        content = path.read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
        if actual != expected:
            errors.append(f"changed {category} file: {name}")

for name, expected in manifest["links"].items():
    path = root / name
    if not path.is_symlink() or str(path.readlink()) != expected:
        errors.append(f"changed source link: {name}")

for name, expected in manifest["submodules"].items():
    result = subprocess.run(["git", "-C", str(root / name), "rev-parse", "HEAD"], capture_output=True, text=True)
    if result.returncode or result.stdout.strip() != expected:
        errors.append(f"wrong dependency pin: {name}")
    alternates = subprocess.run(["git", "-C", str(root / name), "rev-parse", "--git-path", "objects/info/alternates"], capture_output=True, text=True)
    if alternates.returncode == 0 and Path(alternates.stdout.strip()).exists():
        errors.append(f"dependency uses another checkout's objects: {name}")

for name in manifest["adapted"]:
    if not (root / name).is_file():
        errors.append(f"missing adapted file: {name}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"Migration verified: {len(manifest['files'])} files, {len(manifest['preserved'])} preserved files, {len(manifest['submodules'])} dependency pins.")
