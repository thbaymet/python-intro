import unittest
import strings


class TestStrings(unittest.TestCase):

    def test_capitalize_one_word(self):
        """
        Tests capitalize function with a single word
        :return: True if the result is expected value, False else
        """
        self.assertEqual(strings.capitalize("python"), "Python")
