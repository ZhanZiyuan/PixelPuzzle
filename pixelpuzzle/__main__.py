#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Encode/decode images using Base64
or shuffle/recover the pixels of images.
"""

import sys
from pathlib import Path

from pixelpuzzle import main

if __package__ is None and not getattr(sys, "frozen", False):
    path = Path(__file__).resolve()
    sys.path.insert(0, str(path.parent.parent))

if __name__ == "__main__":

    main()
