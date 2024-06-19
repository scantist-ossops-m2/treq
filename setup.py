
from setuptools import setup

# Per setuptools' documentation, incremental's plugin for setting the version
# is only accessible if an imperative setup.py is present.

# https://setuptools.pypa.io/en/latest/userguide/extension.html#adding-arguments

setup(use_incremental=True)
