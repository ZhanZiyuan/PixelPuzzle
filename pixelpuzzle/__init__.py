#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Encode/decode images using Base64
or shuffle/recover the pixels of images.
"""

import os
import platform

from .core import decode_base64, encode_base64, recover_pixels, shuffle_pixels

__version__ = "1.0.4"


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
