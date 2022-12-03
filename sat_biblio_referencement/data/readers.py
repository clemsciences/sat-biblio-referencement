

import codecs
import os


__author__ = ["Clément Besnier <clem@clementbesnier.fr>"]


def read_text(directory, filename):
    with codecs.open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
        return f.read()


def split_page(text):
    return [i.replace("\n", " ") for i in text.split(".\n")]