import csv
from enum import Enum
import os

from PIL import Image

from mosaic_art import calc


class CalcType(Enum):
    """Color Caluculation Type

    * calculate average color
    * calculate median color
    * calculate mode color
    """
    AVERAGE = 1
    MEDIAN  = 2
    MODE    = 3

class ColorCalculator:
    pass


def main():
    calculator = ColorCalculator()
    calculator.type = CalcType.AVERAGE
    print(type(calculator))

if __name__ == '__main__':
    main()
