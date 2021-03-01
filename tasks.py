#!/usr/bin/env python3

import os
from glob import glob
from invoke import task


@task
def install(c):
    """
    Install python build requirements.
    """
    c.run("pip install -U pip setuptools pip-tools")


@task
def update_packages(c):
    """
    Update python dependencies.
    """
    cwd = os.path.join(os.path.dirname(__file__))
    for filepath in glob(os.path.join(cwd, "requirements*.in")):
        c.run(f"pip-compile --reuse-hashes --generate-hashes --allow-unsafe {filepath}")