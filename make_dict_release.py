"""Build the dictionary package for the GitHub repo: copies the files and writes manifest.json."""
import hashlib, json, os, shutil, sys
src, out, version = sys.argv[1], sys.argv[2], sys.argv[3]
notes = sys.argv[4] if len(sys.argv) > 4 else ""
os.makedirs(out, exist_ok=True)
files = {}
for name in ["uz_UZ-2026.aff", "uz_UZ-2026.dic", "freq.txt"]:
    if os.path.abspath(src) != os.path.abspath(out):
        shutil.copyfile(os.path.join(src, name), os.path.join(out, name))
    data = open(os.path.join(out, name), "rb").read()
    files[name] = {"sha256": hashlib.sha256(data).hexdigest(), "size": len(data)}
m = {"version": version, "min_app": "1.6.0", "notes": notes, "files": files}
open(os.path.join(out, "manifest.json"), "w").write(json.dumps(m, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(m, indent=1, ensure_ascii=False))
