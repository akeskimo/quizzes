#!/usr/bin/env python3

import subprocess
import sys

output = subprocess.check_output("git diff --cached --raw".split())
if len(output) == 0:
    sys.exit(0)

staged_files = {f.split("\t")[1] for f in output.rstrip().decode().split("\n")}

# Instead of hardcoding the patterns the testing could be driven
# by the build-system.
runnermap= {
    "make pytest": ["python/"],
    "make cpptest": ["cpp/"]
}

executables = set()
for filepath in staged_files:
    for runner, startpatterns in runnermap.items():
        if any([filepath.startswith(p) for p in startpatterns]):
            executables.add(runner)

for executable in executables:
    subprocess.check_call(executable.split())
