import os
from setuptools import setup, find_packages

setup(
  name = "StackLang",
  version = "0.0.1",
  author = "Aaron Young",
  scripts = ["StackLang.py"],
  packages = find_packages(),
  install_requires = ["click==6.7"],
)
