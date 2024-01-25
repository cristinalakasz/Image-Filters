"""numpy implementation of image filters"""
from __future__ import annotations

import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale using numpy

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)

    # Use numpy slicing in order to have fast vectorized code
    gray_image[:, :, 0] = gray_image[:, :, 1] = gray_image[:, :, 2] = 0.21*image[:, :, 0] + 0.72 * \
        image[:, :, 1] + 0.07*image[:, :, 2]
    # Convert the values back to integers, as after applying the grayscale function the image likely contains floating point numbers
    gray_image = gray_image.astype("uint8")
    # Return image
    return gray_image


def numpy_color2sepia(image: np.array, k: float = 1) -> np.array:
    """Convert rgb pixel array to sepia using numpy

    Args:
        image (np.array)
        k (float): amount of sepia (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
        you may ignore it)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = np.empty_like(image)

    # define sepia matrix (optional: with stepless sepia changes)
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ]
    # convert sepia matrix to numpy array
    sepia_matrix = np.array(sepia_matrix)

    # build the tuneable sepia matrix by scaling the original sepia matrix with matrix k
    identity = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    sepia_matrix = identity * (1-k) + sepia_matrix * k
    # sepia_matrix = [
    #    [0.393 + 0.607*(1 - k), 0.769 - 0.769 * (1-k), 0.189 - 0.189 * (1-k)],
    #    [0.349 - 0.349*(1-k), 0.686 + 0.314 * (1-k), 0.168 - 0.168 * (1-k)],
    #    [0.272 - 0.272 * (1-k), 0.534 - 0.534*(1-k), 0.131 + 0.869*(1-k)],
    # ]

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter
    sepia_image = np.einsum("ijk,lk->ijl", image, sepia_matrix)

    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    sepia_image[np.where(sepia_image > 255)] = 255

    # Convert to the right type
    sepia_image = sepia_image.astype("uint8")

    # Return image
    return sepia_image
