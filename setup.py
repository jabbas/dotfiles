# -*- coding: utf-8 -*-
# Author: Grzegorz Dziegielewski

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dotfiles",
    version = "0.1",
    author = "Grzegorz Dzięgielewski",
    author_email = "jabbas@jabbas.eu",
    description = "simple wrapper over git to manage dotfiles",
    license = "GPLv3+",
    keywords = "dotfiles git wrapper",
    url = "http://git.jabbas.eu/dotfiles.git",
    packages = find_packages(),
    entry_points = { "console_scripts": ["dtf = dotfiles:main"] },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Utilities",
        "Topic :: Software Development :: Version Control",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
)
