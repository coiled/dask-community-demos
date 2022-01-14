"""
Script written by ian-r-rose to pull new contributors to Dask and Distributed.

Caveats: (1) must have tags locally (git fetch upstream --tags),
(2) must be run from a super directory which has the relevant repos as siblings,
(3) repo must be up to date
"""



from __future__ import annotations
import subprocess

BEFORE = "2021.12.0"
AFTER = "main"
repos = ["dask", "distributed"]

before: set[str] = set()
after: set[str] = set()

for r in repos:

    out = (
        subprocess.run(
            ["git", "shortlog", "-n", "-s", BEFORE],
            capture_output=True,
            cwd=r,
        )
        .stdout
        .decode()
        .strip()
        .split("\n")
    )
    before |= {o.split("\t")[1] for o in out}
    out = (
        subprocess.run(
            ["git", "shortlog", "-n", "-s", f"{BEFORE}..{AFTER}"],
            capture_output=True,
            cwd=r,
        )
        .stdout
        .decode()
        .strip()
        .split("\n")
    )
    after |= {o.split("\t")[1] for o in out}

print(f"{len(after)} contributors for this release: {after}\n\n")
print(f"{len(after - before)} new contributors for this release: {after - before}")


