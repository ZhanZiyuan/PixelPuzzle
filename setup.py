#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Encode/decode images using Base64
or shuffle/recover the pixels of images.
"""

from setuptools import find_packages, setup

setup(
    name="PixelPuzzle",
    version="0.4.0",
    description=(
        "Encode/decode images using Base64 "
        "or shuffle/recover the pixels of images."
    ),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="ZhanZiyuan",
    author_email="ziyuanzhan@mail.nankai.edu.cn",
    maintainer="ZhanZiyuan",
    maintainer_email="ziyuanzhan@mail.nankai.edu.cn",
    url="https://github.com/ZhanZiyuan/PixelPuzzle",
    packages=find_packages(),
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Security :: Cryptography",
    ],
    license="GNU GPLv3",
    python_requires=">=3.10",
    install_requires=[
        "numpy>=2.2.4",
        "pillow>=11.1.0",
    ],
    entry_points={
        "console_scripts": [
            "pixelpuzzle=pixelpuzzle.__main__:main",
        ],
    },
)
