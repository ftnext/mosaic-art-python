from unittest import TestCase

from mosaic_art import args_validation


class TestValidColorRepresentaton(TestCase):
    """Test of function `valid_color_representation`"""

    def test_specify_average():
        """Test of specifying average as representation"""
        actual = args_validation.valid_color_representation('average')
        self.assertTrue(actual)

    def test_specify_median():
        """Test of specifying median as representation"""
        actual = args_validation.valid_color_representation('median')
        self.assertTrue(actual)

    def test_specify_mode():
        """Test of specifying mode as representation"""
        actual = args_validation.valid_color_representation('mode')
        self.assertTrue(actual)

    def test_specify_short_spelling():
        """Test of specifying with short spelling"""
        actual = args_validation.valid_color_representation('averge')
        self.assertFalse(actual)

    def test_specify_long_spelling():
        """Test of specifying with long spelling"""
        actual = args_validation.valid_color_representation('modee')
        self.assertFalse(actual)

    def test_specify_wrong_spelling():
        """Test of specifying with long spelling"""
        actual = args_validation.valid_color_representation('medain')
        self.assertFalse(actual)

    def test_specify_other_word():
        """Test of specifying with long spelling"""
        actual = args_validation.valid_color_representation('hoge')
        self.assertFalse(actual)
