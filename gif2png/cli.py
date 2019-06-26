import os.path

import click

from .core import get_frames, save_frames


@click.command()
@click.option('-f', '--filename', help='Gif want to converte')
@click.option('-p', '--path', default='./images', help='Saved directory')
def gif2png(filename, path):
    frames = get_frames(filename)
    name = os.path.splitext(filename)[0]
    save_frames(frames, name, path)


if __name__ == '__main__':
    gif2png()
