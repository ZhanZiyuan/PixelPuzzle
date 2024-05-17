#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import platform
from base64 import b64decode, b64encode
from pathlib import Path
from typing import Union

import numpy as np
from PIL import Image


def encode_base64(image_to_encode: str,
                  encoded_text: Union[str, Path] = Path(__file__).with_suffix(".txt")) -> None:
    """
    Encode the input image as a Base64 string.
    """
    with open(image_to_encode, "rb") as image_file:
        encoded_string = b64encode(image_file.read()).decode("utf-8")
        with open(encoded_text, "w", encoding="utf-8") as text_file:
            text_file.write(encoded_string)


def decode_base64(encoded_text: str,
                  decoded_image: Union[str, Path] = Path(__file__).with_suffix(".png")) -> None:
    """
    Decode the input Base64 string into an image.
    """
    with open(encoded_text, "r", encoding="utf-8") as text_file:
        decoded_output = b64decode(text_file.read())
        with open(decoded_image, "wb") as image_file:
            image_file.write(decoded_output)


def shuffle_pixels(origin_image: str,
                   shuffled_image: str,
                   index_file: Union[str, Path] = Path(__file__).with_suffix(".npy"),
                   dimension: int = 0,
                   seed: Union[int, None] = None) -> None:
    """
    Shuffle the arrangement of pixels in a specified dimension.
    """
    rng = np.random.default_rng(seed)

    pixel_array = np.array(
        Image.open(origin_image)
    )
    indices_shuffled = rng.permutation(
        pixel_array.shape[dimension]
    )

    np.save(index_file, indices_shuffled)

    shuffled_output = Image.fromarray(
        np.take(
            pixel_array,
            indices_shuffled,
            axis=dimension
        )
    )
    shuffled_output.save(shuffled_image)


def recover_pixels(shuffled_image: str,
                   recovered_image: str,
                   index_file: Union[str, Path] = Path(__file__).with_suffix(".npy"),
                   dimension: int = 0) -> None:
    """
    Recover the arrangement of pixels in a specified dimension.
    """
    pixel_array = np.array(
        Image.open(shuffled_image)
    )

    indices_recovered = np.argsort(
        np.load(index_file)
    )

    recovered_output = Image.fromarray(
        np.take(
            pixel_array,
            indices_recovered,
            axis=dimension
        )
    )
    recovered_output.save(recovered_image)


if __name__ == "__main__":

    print(
        "A script to encode/decode images "
        "or shuffle/recover the pixels of images.\n"
    )

    selection_of_mode = input(
        'Please select one mode.\n'
        'Options are "encode", "decode", "shuffle" and "recover".\n'
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
            path_of_output_array = input(
                "Please input the path of the output array.\n"
            )
            dimension_to_shuffle = input(
                "Please input the dimension to shuffle.\n"
            )
            random_number_seed = input(
                'Please input the selected random number seed.\n'
                'Type "no" for `None`.\n'
            )
            shuffle_pixels(
                path_of_original_image,
                path_of_shuffled_image,
                path_of_output_array,
                int(dimension_to_shuffle),
                seed=None if random_number_seed == "no" else int(random_number_seed)
            )

        case "recover":
            path_of_shuffled_image = input(
                "Please input the path of the shuffled image.\n"
            )
            path_of_recovered_image = input(
                "Please input the path of the recovered image.\n"
            )
            path_of_input_array = input(
                "Please input the path of the input array.\n"
            )
            dimension_to_recover = input(
                "Please input the dimension to recover.\n"
            )
            recover_pixels(
                path_of_shuffled_image,
                path_of_recovered_image,
                path_of_input_array,
                int(dimension_to_recover)
            )

        case _:
            print("Invalid mode selection.\n")

    if platform.system() == "Windows":
        os.system("pause")
    else:
        os.system(
            "/bin/bash -c 'read -s -n 1 -p \"Press any key to exit.\"'"
        )
        print()
