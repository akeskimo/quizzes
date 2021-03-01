#!/usr/bin/env python3

from setuptools import setup

setup(
    name="quizzes",
    version="0.0",
    description="Python programming brain-teasers with build-system.",
    author="Aapo Keskimolo",
    author_email="aapokesk@gmail.com",
    url="https://github.com/akeskimo/quizzes",
    install_requires=[
        "invoke>=1.5.0",
        "pytest>=6.2.2",
        "pip-tools>=5.5.0"
    ],
    packages=["packages"]
)