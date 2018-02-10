import csv
from enum import Enum
import os
import sys

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
    args = sys.argv
    if len(args) != 2:
        print('[Error] Arguments Number:')
        print('    Usage: python calculate_material_color.py calc_type')
        sys.exit('    calc_type can take the following values: average, median, mode')
    calc_type = type_from_args(args[1])
    if calc_type is None:
        print('[Error] Invalid argument:')
        print('    Usage: python calculate_material_color.py calc_type')
        sys.exit('    calc_type can take the following values: average, median, mode')

    calculator = ColorCalculator(calc_type)
    print(calculator.calc_func)

def type_from_args(string):
    """Return CalcType object corresponding to string

    Args:
        string: Suppose the first command line arguments (args[1])

    Returns:
        CalcType object
    """
    if string == 'average':
        return CalcType.AVERAGE
    elif string == 'median':
        return CalcType.MEDIAN
    elif string == 'mode':
        return CalcType.MODE
    else:
        return None

if __name__ == '__main__':
    main()
