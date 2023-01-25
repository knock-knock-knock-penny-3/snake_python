""" docstring """

import os
import sys

from pygame.image import load
from pygame.mixer import Sound
from pygame.transform import scale

def get_sprite(filename, size, alpha=True):
    """ docstring """
    path = f'assets/sprites/{filename}'
    sprite = scale(load(resource_path(path)), size)

    if alpha:
        return sprite.convert_alpha()
    return sprite.convert()

def get_sound(filename):
    """ docstring """
    path = f'assets/sounds/{filename}'
    return Sound(resource_path(path))

def resource_path(relative_path):
    """ docstring """
    if hasattr(sys, '_MEIPASS'):
        base = getattr(sys, '_MEIPASS')
        return os.path.join(base, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
