from __future__ import annotations

import time
from typing import Callable

from . import get_filter, io


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    # run the filter function `calls` times
    # return the _average_ time of one call
    times = []
    for i in range(calls):
        start_time = time.time()
        filter_function(*arguments)
        end_time = time.time()
        times.append(end_time - start_time)
    avarage_runtime = sum(times)/calls
    return avarage_runtime


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """
    # save the report in timing-report.txt
    with open("timing-report.txt", "w") as file:

        # load the image
        image = io.read_image(filename)

        # show the image being used, including its dimensions
        print(f"Image: {filename} ({image.shape[0]}x{image.shape[1]})")
        file.write(
            f"Image: {filename} ({image.shape[0]}x{image.shape[1]})\n\n")

        # iterate through the filters
        filter_names = ["color2gray", "color2sepia"]
        for filter_name in filter_names:
            # get the reference filter function
            reference_filter = get_filter(filter_name, "python")
            # time the reference implementation
            start_time = time.time()
            reference_filter(image)
            end_time = time.time()
            reference_time = end_time - start_time
            print(
                f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})"
            )
            file.write(f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})\n"
                       )
            # iterate through the implementations
            implementations = ["numpy", "numba"]
            for implementation in implementations:
                filter = get_filter(filter_name, implementation)
                # run the filter once before timing to compile
                filter(image)
                # time the filter
                start_time = time.time()
                filter(image)
                end_time = time.time()
                filter_time = end_time - start_time
                filter_time += 1e-9  # avoid division by zero
                # compare the reference time to the optimized time
                speedup = reference_time / filter_time
                print(
                    f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
                )
                file.write(
                    f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)\n")


if __name__ == "__main__":
    # run as `python -m in3110_instapy.timing`
    make_reports()
