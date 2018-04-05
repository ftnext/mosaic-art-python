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

class TestMosaicArtFileName(TestCase):
    """Test of function `mosaic_art_file_name` """

    def test_average_average_prefix(self):
        """Test of file name prefix in specifying average color
        as target representation and material representation"""
        expected = 'test_file_mosaic_average_average_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'average', 'average')
        self.assertTrue(actual.startswith(expected))

    def test_average_median_prefix(self):
        """Test of file name prefix
        in specifying average color as target representation
        and median color as material representation"""
        expected = 'test_file_mosaic_average_median_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'average', 'median')
        self.assertTrue(actual.startswith(expected))

    def test_average_mode_prefix(self):
        """Test of file name prefix
        in specifying average color as target representation
        and mode color as material representation"""
        expected = 'test_file_mosaic_average_mode_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'average', 'mode')
        self.assertTrue(actual.startswith(expected))

    def test_median_average_prefix(self):
        """Test of file name prefix
        in specifying median color as target representation
        and average color as material representation"""
        expected = 'test_file_mosaic_median_average_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'median', 'average')
        self.assertTrue(actual.startswith(expected))

    def test_median_median_prefix(self):
        """Test of file name prefix in specifying median color
        as target representation and material representation"""
        expected = 'test_file_mosaic_median_median_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'median', 'median')
        self.assertTrue(actual.startswith(expected))

    def test_median_mode_prefix(self):
        """Test of file name prefix
        in specifying median color as target representation
        and mode color as material representation"""
        expected = 'test_file_mosaic_median_mode_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'median', 'mode')
        self.assertTrue(actual.startswith(expected))

    def test_mode_average_prefix(self):
        """Test of file name prefix
        in specifying mode color as target representation
        and average color as material representation"""
        expected = 'test_file_mosaic_mode_average_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'mode', 'average')
        self.assertTrue(actual.startswith(expected))

    def test_mode_median_prefix(self):
        """Test of file name prefix
        in specifying mode color as target representation
        and median color as material representation"""
        expected = 'test_file_mosaic_mode_median_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'mode', 'median')
        self.assertTrue(actual.startswith(expected))

    def test_mode_mode_prefix(self):
        """Test of file name prefix in specifying mode color
        as target representation and material representation"""
        expected = 'test_file_mosaic_mode_mode_'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'mode', 'mode')
        self.assertTrue(actual.startswith(expected))

    def test_average_average_suffix(self):
        """Test of file name suffix in specifying average color
        as target representation and material representation"""
        expected = '.png'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'average', 'average')
        self.assertTrue(actual.endswith(expected))

    def test_median_mode_suffix(self):
        """Test of file name suffix
        in specifying median color as target representation
        and mode color as material representation"""
        expected = '.png'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'median', 'mode')
        self.assertTrue(actual.endswith(expected))

    def test_mode_average_suffix(self):
        """Test of file name suffix
        in specifying mode color as target representation
        and average color as material representation"""
        expected = '.png'
        actual = make_mosaic_art.mosaic_art_file_name(
                    'test_file.png', 'mode', 'average')
        self.assertTrue(actual.endswith(expected))
