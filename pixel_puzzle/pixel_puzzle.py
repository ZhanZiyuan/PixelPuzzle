#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Encode/decode images using Base64
or shuffle/recover the pixels of images.
"""

import hashlib
import os
import platform
import secrets
from base64 import b64decode, b64encode
from pathlib import Path

import numpy as np
from PIL import Image


def encode_base64(image_to_encode: str | Path,
                  encoded_text: str | Path = Path(__file__).with_suffix(".txt")) -> None:
    """
    Encode the input image as a Base64 string.
    """
    with open(image_to_encode, "rb") as image_file:
        encoded_string = b64encode(image_file.read()).decode("utf-8")
        with open(encoded_text, "w", encoding="utf-8") as text_file:
            text_file.write(encoded_string)


def decode_base64(encoded_text: str | Path,
                  decoded_image: str | Path = Path(__file__).with_suffix(".png")) -> None:
    """
    Decode the input Base64 string into an image.
    """
    with open(encoded_text, "r", encoding="utf-8") as text_file:
        decoded_output = b64decode(text_file.read())
        with open(decoded_image, "wb") as image_file:
            image_file.write(decoded_output)


def shuffle_pixels(origin_image: str | Path,
                   shuffled_image: str | Path,
                   seed: int | None = None,
                   index_file: str | Path | None = Path(__file__).with_suffix(".npz"),
                   image_quality: str = "high") -> None:
    """
    Shuffle the arrangement of pixels.
    """
    scale_of_image_quality = {
        "low": 30,
        "medium": 75,
        "high": 95
    }

    rng = np.random.default_rng(seed)

    pixel_array = np.array(Image.open(origin_image))
    image_size = pixel_array.shape
    flat_pixels = pixel_array.reshape(-1, image_size[2])
    pixel_indices = np.arange(flat_pixels.shape[0])

    rng.shuffle(pixel_indices)

    if seed is None and index_file is not None:
        np.savez_compressed(
            index_file,
            pixel_indices=pixel_indices,
            image_size=image_size
        )

    shuffled_output = Image.fromarray(
        flat_pixels[pixel_indices].reshape(image_size)
    )
    shuffled_output.save(
        shuffled_image,
        quality=scale_of_image_quality[image_quality],
        optimize=True,
        progressive=True,
        compress_level=9
    )


def recover_pixels(shuffled_image: str | Path,
                   recovered_image: str | Path,
                   seed: int | None = None,
                   index_file: str | Path | None = Path(__file__).with_suffix(".npz"),
                   image_quality: str = "high") -> None:
    """
    Recover the arrangement of pixels.
    """
    scale_of_image_quality = {
        "low": 30,
        "medium": 75,
        "high": 95
    }

    pixel_array = np.array(Image.open(shuffled_image))
    image_size = pixel_array.shape
    flat_pixels = pixel_array.reshape(-1, image_size[2])

    if seed is not None and index_file is None:
        rng = np.random.default_rng(seed)
        pixel_indices = np.arange(flat_pixels.shape[0])
        rng.shuffle(pixel_indices)
    elif seed is None and index_file is not None:
        indices_data = np.load(index_file)
        pixel_indices = indices_data["pixel_indices"]
        image_size = tuple(indices_data["image_size"])

    recovered_indices = np.argsort(pixel_indices)

    recovered_output = Image.fromarray(
        flat_pixels[recovered_indices].reshape(image_size)
    )
    recovered_output.save(
        recovered_image,
        quality=scale_of_image_quality[image_quality],
        optimize=True,
        progressive=True,
        compress_level=9
    )


def generate_secure_seed(method: str = "os",
                         passphrase: str | None = None) -> int:
    """
    Generate a secure 128-bit random seed.
    """
    match method:
        case "os":
            return int.from_bytes(os.urandom(16), "big")

        case "secrets":
            return secrets.randbits(128)

        case "hash":
            if passphrase is None:
                raise ValueError(
                    'The "hash" method requires a non-empty passphrase string.'
                )
            hash_hex = hashlib.sha256(passphrase.encode("utf-8")).hexdigest()
            return int(hash_hex, 16) % (2**128)

        case _:
            raise ValueError(
                'Unsupported method. '
                'Choose from "os", "secrets", or "hash".'
            )


def main() -> None:
    """
    The main function.
    """
    print(
        "A script to encode/decode images "
        "or shuffle/recover the pixels of images.\n"
    )

    selection_of_mode = input(
        'Please select one mode.\n'
        'Options are "encode", "decode", "shuffle" or "recover".\n'
    )

    match selection_of_mode:

        case "encode":
            path_of_original_image = input(
                "Please input the path of the original image.\n"
            )
            path_of_output_text = input(
                "Please input the path of the output text file.\n"
            )
            encode_base64(
                path_of_original_image,
                path_of_output_text
            )

        case "decode":
            path_of_input_text = input(
                "Please input the path of the input text file.\n"
            )
            path_of_decoded_image = input(
                "Please input the path of the decoded image.\n"
            )
            decode_base64(
                path_of_input_text,
                path_of_decoded_image
            )

        case "shuffle":
            path_of_original_image = input(
                "Please input the path of the original image.\n"
            )
            path_of_shuffled_image = input(
                "Please input the path of the shuffled image.\n"
            )
            while True:
                random_number_seed = input(
                    'Please input the selected random number seed.\n'
                    'Type "no" for `None`.\n'
                )
                if random_number_seed == "no":
                    path_of_output_arrays = input(
                        "Please input the path of the output arrays.\n"
                    )
                    break
                try:
                    int(random_number_seed)
                    break
                except ValueError:
                    print(
                        "Invalid input. Please try again. "
                        "Please input a non-negative integer. "
                    )
            while True:
                level_of_image_quality = input(
                    'Please select the level of image quality.\n'
                    'Options are "low", "medium" or "high".\n'
                )
                if level_of_image_quality in ["low", "medium", "high"]:
                    break
                else:
                    print(
                        'Invalid input. Please try again. '
                        'Options are "low", "medium" or "high". '
                    )
            shuffle_pixels(
                path_of_original_image,
                path_of_shuffled_image,
                None if random_number_seed == "no" else int(random_number_seed),
                None if random_number_seed != "no" else path_of_output_arrays,
                level_of_image_quality
            )

        case "recover":
            path_of_shuffled_image = input(
                "Please input the path of the shuffled image.\n"
            )
            path_of_recovered_image = input(
                "Please input the path of the recovered image.\n"
            )
            while True:
                random_number_seed = input(
                    'Please input the selected random number seed.\n'
                    'Type "no" for `None`.\n'
                )
                if random_number_seed == "no":
                    path_of_input_arrays = input(
                        "Please input the path of the input arrays.\n"
                    )
                    break
                try:
                    int(random_number_seed)
                    break
                except ValueError:
                    print(
                        "Invalid input. Please try again. "
                        "Please input a non-negative integer. "
                    )
            while True:
                level_of_image_quality = input(
                    'Please select the level of image quality.\n'
                    'Options are "low", "medium" or "high".\n'
                )
                if level_of_image_quality in ["low", "medium", "high"]:
                    break
                else:
                    print(
                        'Invalid input. Please try again. '
                        'Options are "low", "medium" or "high". '
                    )
            recover_pixels(
                path_of_shuffled_image,
                path_of_recovered_image,
                None if random_number_seed == "no" else int(random_number_seed),
                None if random_number_seed != "no" else path_of_input_arrays,
                level_of_image_quality
            )

        case _:
            print(
                "Invalid mode selection.\n"
            )

    if platform.system() == "Windows":
        os.system("pause")
    else:
        os.system(
            "/bin/bash -c 'read -s -n 1 -p \"Press any key to exit.\"'"
        )
        print()


if __name__ == "__main__":

    main()
