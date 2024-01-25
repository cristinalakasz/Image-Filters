"""pure Python implementation of image filters"""
from __future__ import annotations

import numpy as np


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale using pure Python

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # Height and width of the image
    height = len(image)
    width = len(image[0])
    # Iterate through the pixels, and apply the grayscale transform
    for i in range(height):
        for j in range(width):
            # Apply the wheights
            gray_image[i, j, 0] = 0.21*image[i, j, 0] + \
                0.72*image[i, j, 1] + 0.07*image[i, j, 2]
            gray_image[i, j, 1] = gray_image[i, j, 0]
            gray_image[i, j, 2] = gray_image[i, j, 0]
    # Convert the values back to integers, as after applying the grayscale function the image likely contains floating point numbers
    gray_image = gray_image.astype("uint8")
    # Return the grayscale image
    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia using pure Python

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ]
    # iterate through the pixels
    # applying the sepia matrix
    for i in range(len(image)):
        for j in range(len(image[0])):
            # applying the sepia matrix
            val0 = sepia_matrix[0][0]*image[i, j, 0] + \
                sepia_matrix[0][1]*image[i, j, 1] + \
                sepia_matrix[0][2]*image[i, j, 2]
            val1 = sepia_matrix[1][0]*image[i, j, 0] + \
                sepia_matrix[1][1]*image[i, j, 1] + \
                sepia_matrix[1][2]*image[i, j, 2]
            val2 = sepia_matrix[2][0]*image[i, j, 0] + \
                sepia_matrix[2][1]*image[i, j, 1] + \
                sepia_matrix[2][2]*image[i, j, 2]
            # set the maximum value to 255 for each channel
            sepia_image[i, j, 0] = min(val0, 255)
            sepia_image[i, j, 1] = min(val1, 255)
            sepia_image[i, j, 2] = min(val2, 255)

    # set the image to the right type
    sepia_image = sepia_image.astype("uint8")

    # Return image
    return sepia_image
