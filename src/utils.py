""" docstring """

from functools import reduce
from operator import add
import os
import sys

from pygame import math
from pygame.font import Font
from pygame.image import load
from pygame.mixer import Sound
from pygame.transform import scale


def get_sprite(filename, size, alpha=True):
    """docstring"""
    path = f"assets/sprites/{filename}"
    sprite = scale(load(_resource_path(path)), size)

    if alpha:
        return sprite.convert_alpha()
    return sprite.convert()


def get_sound(filename):
    """docstring"""
    path = f"assets/sounds/{filename}"
    return Sound(_resource_path(path))


def get_font(filename, size):
    """docstring"""
    path = f"assets/fonts/{filename}"
    return Font(_resource_path(path), size)


def get_path(rel_path):
    """docstring"""
    return _resource_path(rel_path)


def print_text(surface, texts, color=(4, 27, 4)):
    """docstring"""
    interline = 15
    max_height = reduce(add, list(texts.values())) + interline * (len(texts) - 1)
    top = (surface.get_height() - max_height) / 2

    for text, size in texts.items():
        font = Font(_resource_path("assets/fonts/golden_age.ttf"), size)
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect()
        rect.center = math.Vector2(surface.get_width() / 2, top + size / 2)
        surface.blit(text_surface, rect)
        top += size + interline


def _resource_path(relative_path):
    """docstring"""
    if hasattr(sys, "_MEIPASS"):
        base = getattr(sys, "_MEIPASS")
        return os.path.join(base, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
