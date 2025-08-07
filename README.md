<p align="center">
    <img alt="logo" src="https://github.com/ZhanZiyuan/PixelPuzzle/raw/main/assets/logo.svg"
        width="138" />
</p>

# PixelPuzzle

[![GitHub Actions Workflow Status](https://github.com/ZhanZiyuan/PixelPuzzle/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ZhanZiyuan/PixelPuzzle/blob/main/.github/workflows/python-publish.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/ZhanZiyuan/PixelPuzzle)](https://github.com/ZhanZiyuan/PixelPuzzle/commits/main/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pixelpuzzle)](https://pypi.org/project/pixelpuzzle/)
[![PyPI - Version](https://img.shields.io/pypi/v/pixelpuzzle)](https://pypi.org/project/pixelpuzzle/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/pixelpuzzle)](https://pypi.org/project/pixelpuzzle/#files)
[![PyPI Downloads](https://static.pepy.tech/badge/pixelpuzzle/month)](https://pepy.tech/projects/pixelpuzzle)
[![GitHub License](https://img.shields.io/github/license/ZhanZiyuan/PixelPuzzle)](https://github.com/ZhanZiyuan/PixelPuzzle/blob/main/LICENSE)

Encode/decode images using Base64
or shuffle/recover the pixels of images.

## Motivations

This repository is a renewed implementation
of Python code I saw a long time ago on [CoolApk](https://www.coolapk.com/):

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Get the three-dimensional pixel channel matrix of the image
img = np.array(Image.open("C:/Users/user/Downloads/test.png"))
# First dimension
row_len = img.shape[0]

# Shuffle the dimension indices
row_index = np.random.permutation(row_len)
# Generate the chaotic image
img_chaos = img[row_index, :, :]

# Use sorting to unshuffle the image
img_sort = img[np.sort(row_index), :, :]

# Plot the chaotic and unshuffled images
plt.figure("Chaotic and Unshuffled Images")
plt.subplot(121)
plt.imshow(img_chaos)
plt.subplot(122)
plt.imshow(img_sort)
plt.show()
```

And it can also be seen as an implementation
of similar functions of the Android application
[图片混淆](https://www.coolapk.com/feed/27933328?shareKey=N2QxMWY3MTExMDc0NjY0OWQwYWE)
in Python.

## Installation

PixelPuzzle can be installed
from [PyPI](https://pypi.org/project/pixelpuzzle/):

```bash
pip install pixelpuzzle
```

or download the repository and run:

```bash
pip install .
```

as of the repository root folder.

## Examples

- The original image:

    ![The original image](https://github.com/ZhanZiyuan/PixelPuzzle/raw/main/examples/original.png "original")

- The shuffled image (using the random seed `0721`):

    ![The shuffled image](https://github.com/ZhanZiyuan/PixelPuzzle/raw/main/examples/shuffled.png "shuffled")

- The recovered image:

    ![The recovered image](https://github.com/ZhanZiyuan/PixelPuzzle/raw/main/examples/recovered.png "recovered")

## Packaging

The binaries are created with
~~[Nuitka](https://github.com/Nuitka/Nuitka)~~
[PyInstaller](https://github.com/pyinstaller/pyinstaller):

```bash
# Package it on Linux
pyinstaller --name PixelPuzzle --onefile -p pixelpuzzle pixelpuzzle/__main__.py

# Package it on Windows
pyinstaller --name PixelPuzzle --onefile --icon python.ico -p pixelpuzzle pixelpuzzle/__main__.py
```

## Web Applications

Deploy [Pixel Puzzle](https://pixelpuzzle-web.vercel.app/)
on [Vercel](https://github.com/vercel/vercel).

## Similar Projects

Here are some links to other similar projects that I am aware of:

- [PicEncryptApp](https://github.com/goldsudo/PicEncryptApp)
- [piConfuse](https://github.com/Conyrol/piConfuse)
- [Jencryption](https://github.com/Jinnrry/Jencryption)
- [RicEncrypt](https://github.com/NaviHX/ricencrypt)

## Copyrights

PixelPuzzle is a free, open-source software package
(distributed under the [GPLv3 license](./LICENSE)).
The sample image used is downloaded from
[satchely doki doki literature club! natsuki](https://yande.re/post/show/465068).
The Python icon is downloaded from
[python.ico](https://github.com/python/cpython/blob/main/PC/icons/python.ico).
