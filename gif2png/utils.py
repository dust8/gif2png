import errno
import os


def ensure_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as ex:
        if ex.errno != errno.EEXIST:
            raise ex
