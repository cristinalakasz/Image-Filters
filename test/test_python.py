from in3110_instapy.python_filters import python_color2gray, python_color2sepia


def test_color2gray(image):
    """Check on the return values of the grayscale python filter.
    Checks that the filter function returns numpy arrays with the expected shape and dtype. 
    Checks that the filters have been applied correctly to the pixels. (checked on a few selected pixels)

    Parameters:
        - image (np array): np array of the image on which to be applied the filter
    Returns:
    None
    """
    # run color2gray
    gray_image = python_color2gray(image)
    # check that the result has the right shape, type
    assert image.shape == gray_image.shape, "The grayscale image shape does not match the original image shape"
    assert image.dtype == gray_image.dtype, "The grayscale image type does not match the original image type"
    # assert uniform r,g,b values for some pixels
    selected_pixels = [(0, 0), (10, 10), (5, 7), (1, 1), (1, 3)]
    for i, j in selected_pixels:
        assert gray_image[i, j, 0] == gray_image[i, j, 1] == gray_image[i,
                                                                        j, 2], f"The r,g,b values are not uniform at pixel ({i}, {j})."
    # check that the pixel values are the correct ones
    for i, j in selected_pixels:
        expected_value = 0.21*image[i, j, 0] + \
            0.72*image[i, j, 1] + 0.07*image[i, j, 2]
        assert gray_image[i, j, 0] == expected_value.astype(
            "uint8"), f"The r,g,b values are not correct at pixel ({i}, {j})."


def test_color2sepia(image):
    """Check on the return values of the sepia python filter.
    Checks that the filter function returns numpy arrays with the expected shape and dtype. 
    Checks that the filters have been applied correctly to the pixels. (checked on a few selected pixels)

    Parameters:
        - image (np array): np array of the image on which to be applied the filter
    Returns:
    None
    """
    # run color2sepia
    sepia_image = python_color2sepia(image)
    # check that the result has the right shape, type
    assert image.shape == sepia_image.shape, "The sepia image shape does not match the original image shape"
    assert image.dtype == sepia_image.dtype, "The sepia image type does not match the original image type"
    # verify some individual pixel samples
    selected_pixels = [(0, 0), (10, 10), (5, 7), (1, 1), (1, 3)]
    # according to the sepia matrix
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ]
    # check that the pixel values are the correct ones
    for i, j in selected_pixels:
        expected_value = sepia_matrix[0][0]*image[i, j, 0] + \
            sepia_matrix[0][1]*image[i, j, 1] + \
            sepia_matrix[0][2]*image[i, j, 2]
        if expected_value > 255:
            expected_value = 255
        assert sepia_image[i, j, 0] == expected_value.astype(
            "uint8"), f"The r,g,b values are not correct at pixel ({i}, {j})."
        expected_value = sepia_matrix[1][0]*image[i, j, 0] + \
            sepia_matrix[1][1]*image[i, j, 1] + \
            sepia_matrix[1][2]*image[i, j, 2]
        if expected_value > 255:
            expected_value = 255
        assert sepia_image[i, j, 1] == expected_value.astype(
            "uint8"), f"The r,g,b values are not correct at pixel ({i}, {j})."
        expected_value = sepia_matrix[2][0]*image[i, j, 0] + \
            sepia_matrix[2][1]*image[i, j, 1] + \
            sepia_matrix[2][2]*image[i, j, 2]
        if expected_value > 255:
            expected_value = 255
        assert sepia_image[i, j, 2] == expected_value.astype(
            "uint8"), f"The r,g,b values are not correct at pixel ({i}, {j})."
