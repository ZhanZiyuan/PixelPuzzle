# PixelPuzzle

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
plt.figure('Chaotic and Unshuffled Images')
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

## Examples

- The original image:

    ![The original image](./assets/original.png "original")

- The shuffled image:

    ![The shuffled image](./assets/shuffled.png "shuffled")

    The `.npz` file [key.npz](./assets/key.npz) stores the original positions of pixels.

- The recovered image:

    ![The recovered image](./assets/recovered.png "recovered")

## Packaging

The binaries are created with
[Nuitka](https://github.com/Nuitka/Nuitka):

```bash
# Package it on Linux
python -m nuitka --onefile --remove-output pixel_puzzle.py

# Package it on Windows
python -m nuitka --onefile --remove-output --windows-icon-from-ico="python.ico" pixel_puzzle.py
```

## TODO

Deploy web applications using:

- [Vercel](https://github.com/vercel/vercel)
- [Gradio](https://github.com/gradio-app/gradio)
- [Streamlit](https://github.com/streamlit/streamlit)

## Similar Projects

Here are some links to other similar projects that I am aware of:

- [PicEncryptApp](https://github.com/goldsudo/PicEncryptApp)
- [piConfuse](https://github.com/Conyrol/piConfuse)
- [Jencryption](https://github.com/Jinnrry/Jencryption)
- [RicEncrypt](https://github.com/NaviHX/ricencrypt)

## Copyrights

PixelPuzzle is a free, open-source software package
(distributed under the [GPLv3 license](./LICENSE)).
Some of the references are as follows:

- [CPython](https://github.com/python/cpython)
- [Nuitka](https://github.com/Nuitka/Nuitka)
- [Doki Doki Literature Club (DDLC)](https://ddlc.moe/)
- [图片混淆](https://www.coolapk.com/feed/27933328?shareKey=N2QxMWY3MTExMDc0NjY0OWQwYWE)

[The Python Software Foundation](https://www.python.org/psf-landing/)
owns the copyright of [Python icon](./assets/python.ico).
The sample image used is downloaded from
[satchely doki doki literature club! natsuki](https://yande.re/post/show/465068).
