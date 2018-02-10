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
    def __init__(self, calc_type):
        self.calc_func = ColorCalculator.calculate_function(calc_type)
        self.csv_name = ColorCalculator.color_csv_name(calc_type)

    def calculate_function(calc_type):
        """Return function corresponding to color calculation type

        Args:
            calc_type: CalcType object

        Returns:
            color calculation function (in calc module)
        """
        if calc_type is CalcType.AVERAGE:
            return calc.average_color_in_range
        elif calc_type is CalcType.MEDIAN:
            return calc.median_color_in_range
        else: # calc_type is CalcType.MODE:
            return calc.mode_color_in_range

    def color_csv_name(calc_type):
        """Return output csv file name corresponding to color calculation type

        Args:
            calc_type: CalcType object

        Returns:
            output csv file name
        """
        if calc_type is CalcType.AVERAGE:
            return 'average_color.csv'
        elif calc_type is CalcType.MEDIAN:
            return 'median_color.csv'
        else: # calc_type is CalcType.MODE:
            return 'mode_color.csv'

def main():
    calculator = ColorCalculator(CalcType.AVERAGE)
    print(calculator.calc_func)

if __name__ == '__main__':
    main()
