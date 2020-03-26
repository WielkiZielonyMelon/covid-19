import glob
import os

import common

DATA_DIRECTORY = common.DEFAULT_DATA_DIRECTORY
DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, common.DATA_FILENAME_HEADER + "*")


def grab_filenames():
    return glob.glob(DATA_DIRECTORY)

