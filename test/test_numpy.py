import numpy.testing as nt
from in3110_instapy.numpy_filters import numpy_color2gray, numpy_color2sepia



def test_color2gray(image, reference_gray):
    """Check on the return values of the grayscale numpy filter.
    Checks that the filter function returns numpy arrays with the expected shape and dtype. 
    Checks that the filters have been applied correctly to the pixels by comparing the output with the reference grayscale image.

    Parameters:
        - image (np array): np array of the image on which to be applied the filter
    Returns:
    None
    """
    # run color2gray
    gray_image = numpy_color2gray(image)
    # check that the result has the right shape, type
    assert image.shape == gray_image.shape, "The grayscale image shape does not match the original image shape"
    assert image.dtype == gray_image.dtype, "The grayscale image type does not match the original image type"
    # assert uniform r,g,b values
    nt.assert_allclose(gray_image, reference_gray,
                       err_msg="The grayscale filter was not applied correctly.")


def test_color2sepia(image, reference_sepia):
    """Check on the return values of the sepia numpy filter.
    Checks that the filter function returns numpy arrays with the expected shape and dtype. 
    Checks that the filters have been applied correctly to the pixels by comparing the output with the reference grayscale image.

    Parameters:
        - image (np array): np array of the image on which to be applied the filter
    Returns:
    None
    """
    # run color2sepia
    sepia_image = numpy_color2sepia(image)
    # check that the result has the right shape, type
    assert image.shape == sepia_image.shape, "The sepia image shape does not match the original image shape"
    assert image.dtype == sepia_image.dtype, "The sepia image type does not match the original image type"
    # assert uniform r,g,b values
    nt.assert_allclose(sepia_image, reference_sepia, rtol=0.5,
                       err_msg="The sepia filter was not applied correctly.")
