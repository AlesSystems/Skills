#!/usr/bin/env python3
"""Resolve pinned workflow sources and run helpers outside canonical skills."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

SKILL = Path(__file__).resolve().parents[1]
LIBRARY = SKILL.parents[2]
UPSTREAM = LIBRARY / "refs/cursor-plugins"
LOCK = json.loads((SKILL / "references/upstream-lock.json").read_text())


def routes():
    found = dict(LOCK["skills"])
    for relative in LOCK["files"]:
        path = Path(relative)
        if path.suffix != ".md":
            continue
        if path.parent == Path("pstack/skills/poteto-mode/playbooks"):
            found["playbook:" + path.stem] = relative
        elif str(path.parent) in ("pstack/agents", "cursor-team-kit/agents"):
            found["agent:" + path.stem] = relative
    return found


def resolve(name):
    found = routes()
    for key in (name, "pstack:" + name, "cursor-team-kit:" + name):
        if key in found:
            path = UPSTREAM / found[key]
            if not path.is_file():
                raise ValueError(f"Missing dependency: {path}; initialize refs/cursor-plugins at the recorded pin")
            return path
    raise ValueError(f"Unknown dependency {name!r}; use 'list'. Codex built-ins are described in references/codex.md")


def verify():
    sha = subprocess.check_output(["git", "-C", str(UPSTREAM), "rev-parse", "HEAD"], text=True).strip()
    if sha != LOCK["commit"]:
        raise ValueError(f"Upstream pin mismatch: expected {LOCK['commit']}, found {sha}")
    for name, expected in LOCK["files"].items():
        path = UPSTREAM / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f"Missing or modified upstream file: {name}")
    for name in routes():
        resolve(name)
    return {"commit": sha, "skills": len(LOCK["skills"]), "files": len(LOCK["files"]), "routes": len(routes())}


def run_checked(argv, **kwargs):
    subprocess.run([str(a) for a in argv], check=True, **kwargs)


def replace_once(path, old, new):
    text = path.read_text()
    if text.count(old) != 1:
        raise ValueError(f"Adaptation anchor changed in {path.name}; review upstream before continuing")
    path.write_text(text.replace(old, new, 1))


def work_root(value):
    root = Path(value).expanduser().resolve()
    forbidden = [LIBRARY, Path.home() / ".codex", Path.home() / ".Codex", Path.home() / ".agents", Path.home() / ".cursor"]
    if root == Path.home() or any(root == p.resolve() or p.resolve() in root.parents for p in forbidden):
        raise ValueError("Use a task-local work directory outside canonical, installed skill, and runtime folders")
    return root


def prepare(value):
    verify()
    root = work_root(value)
    root.mkdir(parents=True, exist_ok=True)
    bun = shutil.which("bun")
    if bun is None:
        binary = root / "runtime/node_modules/.bin/bun"
        if not binary.exists():
            if not shutil.which("npm"):
                raise ValueError("Bun is absent. Install Node/npm or Bun to prepare executable helpers")
            run_checked(["npm", "install", "--prefix", root / "runtime", "--no-audit", "--no-fund", "bun@1.4.2"], stdout=sys.stderr)
        bun = str(binary)
    digest = hashlib.sha256()
    for path in sorted((SKILL / "scripts").glob("*")):
        if path.is_file():
            digest.update(path.read_bytes())
    source = root / ("tools-" + LOCK["commit"][:12] + "-" + digest.hexdigest()[:12])
    ready = source / ".ready"
    if not ready.exists():
        if source.exists():
            raise ValueError(f"Incomplete preparation at {source}; inspect and remove that generated directory before retrying")
        shutil.copytree(UPSTREAM / "pstack/skills/poteto-mode/scripts", source)
        store = source / "orch/store.ts"
        replace_once(store, 'function resolveFrontier(repo: string): readonly FrontierPr[] {', 'function resolveFrontier(repo: string, pin?: readonly number[]): readonly FrontierPr[] {\n  if (process.env.POTETO_FRONTIER_FORGE === "github") {\n    if (pin === undefined) throw new Error("GitHub frontier requires --prs in bottom-to-top order");\n    return githubFrontier(repo, pin);\n  }')
        replace_once(store, 'const prs = resolveFrontier(repo);', 'const prs = resolveFrontier(repo, pin);')
        store.write_text('import { githubFrontier } from "./github-frontier.ts";\n' + store.read_text())
        for name in ("github-frontier.ts", "github-frontier.test.ts"):
            shutil.copy2(SKILL / "scripts" / name, source / "orch" / name)
        cli = source / "orch/orch.ts"
        replace_once(cli, "manage the Graphite stack frontier", "manage the GitHub or Graphite stack frontier")
        replace_once(cli, "discover the Graphite stack and set the frontier", "resolve the ordered stack and set the frontier")
        replace_once(cli, "optional expected pull request order pin", "bottom-to-top PR list for GitHub; optional order pin for Graphite")
        check = source / "check-plan.mjs"
        replace_once(check, 'Ten lanes on `grok-4.6-fast-xhigh` at the PR head', 'Ten lanes on the configured Codex worker model at the PR head')
        replace_once(check, '["/goal", "git show origin/main:", /30[- ]minute/, "status message"]', '["task acceptance predicate", "read pinned workflow", /30[- ]minute/, "status message"]')
        audit = source / "worktree-audit.sh"
        replace_once(audit, 'transcripts="$HOME/.cursor/projects/$slug/agent-transcripts"', 'transcripts="${POTETO_TRANSCRIPTS_DIR:-/nonexistent-poteto-transcripts}"')
        shutil.copy2(UPSTREAM / "pstack/skills/show-me-your-work/scripts/log.sh", source / "log.sh")
        env = {**os.environ, "BUN_INSTALL_CACHE_DIR": str(root / "bun-cache")}
        run_checked([bun, "install", "--frozen-lockfile"], cwd=source, env=env, stdout=sys.stderr)
        key = hashlib.sha256((source / "package.json").read_bytes() + b"\0" + (source / "bun.lock").read_bytes()).hexdigest()
        (source / "node_modules/.poteto-mode-tools-install-key").write_text(key + "\n")
        ready.write_text(LOCK["commit"] + "\n")
    return {"bun": bun, "scripts": str(source), "work_dir": str(root)}


def run_helper(value, tool, args):
    config = prepare(value)
    source = Path(config["scripts"])
    bun = config["bun"]
    commands = {
        "orch": [bun, source / "orch/orch.ts"],
        "watch-pr": [bun, source / "watch-pr/watch-pr"],
        "check-plan": ["node", source / "check-plan.mjs"],
        "worktree-audit": ["bash", source / "worktree-audit.sh"],
        "log": ["bash", source / "log.sh"],
        "test": [bun, "test", "orch", "watch-pr"],
        "typecheck": [bun, source / "node_modules/typescript/bin/tsc", "--project", source / "watch-pr/tsconfig.json", "--noEmit", "--strict"],
    }
    if tool not in commands:
        raise ValueError("Unknown helper: " + tool)
    env = {**os.environ, "BUN_INSTALL_CACHE_DIR": str(Path(value).resolve() / "bun-cache")}
    if tool == "orch":
        env.setdefault("POTETO_FRONTIER_FORGE", "github")
    if tool == "test":
        env.pop("POTETO_FRONTIER_FORGE", None)
    result = subprocess.run([str(x) for x in commands[tool]] + args, env=env, cwd=source if tool in ("test", "typecheck") else None)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    sub.add_parser("verify")
    item = sub.add_parser("resolve"); item.add_argument("name")
    item = sub.add_parser("prepare"); item.add_argument("--work-dir", required=True)
    item = sub.add_parser("run"); item.add_argument("--work-dir", required=True); item.add_argument("tool"); item.add_argument("args", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    try:
        if args.command == "list":
            for name, path in sorted(routes().items()):
                print(name + "\t" + str(UPSTREAM / path))
        elif args.command == "resolve": print(resolve(args.name))
        elif args.command == "verify": print(json.dumps(verify()))
        elif args.command == "prepare": print(json.dumps(prepare(args.work_dir)))
        else: return run_helper(args.work_dir, args.tool, args.args)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"poteto: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
