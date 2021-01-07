#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Roald Nefs <info@roaldnefs.com>
#
# This file is part of kpn-api-store-python.
#
# kpn-api-store-python is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kpn-api-store-python is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with kpn-api-store-python. If not, see
# <https://www.gnu.org/licenses/>.

from setuptools import setup
from setuptools import find_packages


def get_version() -> str:
    with open("kpnapistore/__init__.py") as file:
        for line in file:
            if line.startswith("__version__"):
                return line.replace("\"", "").split()[-1]


def get_long_description() -> str:
    with open("README.md", "r") as file:
        return file.read()


setup(
    name="kpn-api-store",
    version=get_version(),
    description="Client library for APIs provided by the KPN API Store",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Roald Nefs",
    author_email="info@roaldnefs.com",
    license="LGPLv3",
    url="https://github.com/roaldnefs/kpn-api-store-python",
    packages=find_packages(),
    install_requires=["requests>=2.25.1"],
    python_requires=">=3.6.12",
    entry_points={},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    extras_require={},
)
