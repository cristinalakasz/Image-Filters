# Image Filters package

## Package contents

This package provides **image filters** with different implementations and associated test functions to assert the correctess of them.

The provided filters are:

- grayscale `color2gray`
- sepia `color2sepia`

Each filter is implemented with:

- python
- numpy
- numba

Filters can be accessed as: `{implementation}_{filter}.py`

The package offeres also a function to make a timing report of the different implementations of a filter: `make_reports` in `in3110_instapy/timing.py`, highlighting the performance of numpy and numba with respect to python.

## Installation

To install the package, run the following command: `pip install in3110_instapy`

**Note**: if you encounter weird output like `Successfully built UNKNOWN`, this could be due to out-of-date setuptools and/or a bug in pip’s build isolation. First, make sure to update pip:

```
python3 -m pip install --upgrade setuptools pip # you may want to add --user
```

Then, if that still doesn’t work you may need to add --no-build-isolation to your pip install command:

```
python3 -m pip install --no-build-isolation in3110_instapy
```

If this succeeded, you should be able to pass the package tests:

```
python3 -m pytest -v test/test_package.py
```

Now you can use functions and modules from the package, by importing what you need.

## Usage

To use the filters, call the functions indicating your image path and set the desired arguments:

```
python3 -m in3110_instapy <arguments>

```

where `<arguments>` are:

```
positional arguments:
  file                  The filename to apply filter to

options:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     The output filename
  -g, --gray            Select gray filter
  -se, --sepia          Select sepia filter
  -sc SCALE, --scale SCALE
                        Scale factor to resize image
  -i {python,numba,numpy,cython}, --implementation {python,numba,numpy,cython}
                        The implementation
  -r, --runtime         Track the average runtime spent on the task with the chosen implementation
  -k  KTUNE, --ktune    Tune the sepia filter by changing the k value
```
