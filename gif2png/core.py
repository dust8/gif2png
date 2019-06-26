import os.path

from PIL import Image, ImageSequence

from .utils import ensure_directory


def get_frames(fp):
    im = Image.open(fp)
    return ImageSequence.Iterator(im)


def save_frames(frames, name, path='./images'):
    directory = os.path.join(path, name)
    ensure_directory(directory)

    for index, frame in enumerate(frames):
        filename_png = os.path.join(directory, f'{index}.png')
        frame.save(filename_png)
