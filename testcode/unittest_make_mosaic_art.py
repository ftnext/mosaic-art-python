from unittest import TestCase

from mosaic_art import calc
import make_mosaic_art


class TestMaterialColorFileName(TestCase):
    """Test of function `material_color_file_name` """

    def test_specify_average(self):
        """Test of specifying average color as representative color"""
        expected = 'average_color.csv'
        actual = make_mosaic_art.material_color_file_name('average')
        self.assertEqual(expected, actual)

    def test_specify_median(self):
        """Test of specifying median color as representative color"""
        expected = 'median_color.csv'
        actual = make_mosaic_art.material_color_file_name('median')
        self.assertEqual(expected, actual)

    def test_specify_mode(self):
        """Test of specifying mode color as representative color"""
        expected = 'mode_color.csv'
        actual = make_mosaic_art.material_color_file_name('mode')
        self.assertEqual(expected, actual)

class TestColorCalculateMethod(TestCase):
    """Test of function `color_calculate_method` """

    def test_specify_average(self):
        """Test of specifying average color as representative color"""
        expected = calc.average_color_in_range
        actual = make_mosaic_art.color_calculate_method('average')
        self.assertEqual(expected, actual)

    def test_specify_median(self):
        """Test of specifying median color as representative color"""
        expected = calc.median_color_in_range
        actual = make_mosaic_art.color_calculate_method('median')
        self.assertEqual(expected, actual)

    def test_specify_mode(self):
        """Test of specifying mode color as representative color"""
        expected = calc.mode_color_in_range
        actual = make_mosaic_art.color_calculate_method('mode')
        self.assertEqual(expected, actual)
