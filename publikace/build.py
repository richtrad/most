"""Build the personal MOST Pages tree from one committed, public revision."""
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote, urljoin, urlsplit
import argparse
import html
import json
import os
import re
import shutil
import subprocess

SITE = Path(__file__).resolve().parents[1]
WEB = "https://richtrad.github.io/most/"
PAGES_BUDGET = 932_000_000
LARGE_TYPES = {".glb", ".bin", ".zip", ".blend", ".gltf"}
LINK = re.compile(r"""(?<![\w:-])(href|src|data-src|poster)(\s*=\s*)(["'])([^"'<>]*?)\3""", re.I)
BASE = re.compile(r"""<base\b[^>]*?\bhref\s*=\s*(["'])(.*?)\1""", re.I)
HEAD = re.compile(r"<head(?:\s[^>]*)?>|<html(?:\s[^>]*)?>", re.I)

def git(*args):
    return subprocess.check_output(["git","-C",str(SITE),*args])

def tracked_files():
    files = {}
    for item in git("ls-tree","-rlz","HEAD").split(b"\0"):
        if not item: continue
        info, name = item.split(b"\t",1)
        name = name.decode("utf-8")
        if name.startswith(("publikace/",".github/")): continue
        files[name] = int(info.split()[3])
    return files

def offloaded(files):
    total = sum(files.values())
    remote = {p for p in files if PurePosixPath(p).suffix.lower() in {".gltf",".bin"}}
    total -= sum(files[p] for p in remote)
    for path in sorted(files, key=lambda p: (-files[p],p)):
        if total <= PAGES_BUDGET: break
        if path not in remote and PurePosixPath(path).suffix.lower() in LARGE_TYPES:
            remote.add(path)
            total -= files[path]
    if total > PAGES_BUDGET:
        raise ValueError("Uploaded assets exceed the Pages budget.")
    return remote

def change_html(source, name, remote, raw, script):
    base_tag = BASE.search(source)
    base = urljoin(WEB+quote(name), html.unescape(base_tag[2])) if base_tag else WEB+quote(name)
    def replace(match):
        attr, equals, delim, value = match.groups()
        u = urlsplit(urljoin(base,html.unescape(value)))
        if u.netloc != "richtrad.github.io" or not u.path.startswith("/most/"):
            return match.group()
        path = unquote(u.path[len("/most/"):])
        if path not in remote: return match.group()
        target = raw + quote(path,safe="/")
        if u.query: target += "?" + u.query
        if u.fragment: target += "#" + u.fragment
        return attr + equals + delim + html.escape(target,quote=True) + delim
    source = LINK.sub(replace,source)
    head = re.search(r"<head(?:\s[^>]*)?>",source,re.I) or HEAD.search(source)
    if head:
        return source[:head.end()]+script+source[head.end():]
    raise ValueError("No HTML root for "+name)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    out = parser.parse_args().output.resolve()
    if out == SITE or SITE in out.parents or out in SITE.parents:
        raise SystemExit("Choose a dedicated output outside the source checkout.")
    if out.exists() and any(out.iterdir()):
        raise SystemExit("Choose an empty output directory.")
    if git("status","--porcelain","--untracked-files=no").strip():
        raise SystemExit("Commit your source changes before building.")
    out.mkdir(parents=True,exist_ok=True)
    revision = git("rev-parse","HEAD").decode().strip()
    raw = "https://raw.githubusercontent.com/richtrad/most/"+revision+"/"
    files = tracked_files()
    remote = offloaded(files)
    script_name = "most-assets-"+revision[:12]+".js"
    script = '<script src="/most/'+script_name+'"></script>'
    runtime = (SITE/"publikace/assets.js").read_text("utf-8")
    runtime = runtime.replace("__MOST_LARGE_FILES__",json.dumps(sorted(remote),ensure_ascii=True))
    runtime = runtime.replace("__MOST_RAW_BASE__",raw)
    (out/script_name).write_text(runtime,encoding="utf-8")
    for name in sorted(files):
        if name in remote: continue
        src, dest = SITE/name, out/name
        dest.parent.mkdir(parents=True,exist_ok=True)
        if name.lower().endswith(".html"):
            content = change_html(src.read_bytes().decode("utf-8"),name,remote,raw,script)
            dest.write_bytes(content.encode("utf-8"))
        else:
            shutil.copyfile(src, dest)
    (out/".nojekyll").touch()
    missing = ('<!doctype html><html lang="cs" data-most-asset-route><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1"><title>MOST · 404</title>'
        +script+'</head><body><main><h1>Stránka nenalezena / Page not found</h1>'
        '<p><a id="asset" href="/most/">Zpět na MOST / Return to MOST</a></p></main></body></html>')
    (out/"404.html").write_text(missing,encoding="utf-8")
    print(json.dumps({"revision":revision,"sourceFiles":len(files),"html":sum(n.endswith(".html") for n in files),
                      "largeAssets":len(remote),"staticBytes":sum(p.stat().st_size for p in out.rglob("*") if p.is_file())}))

if __name__=="__main__":
    main()
