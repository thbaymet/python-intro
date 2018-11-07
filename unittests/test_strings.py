import unittest
import strings


class TestStrings(unittest.TestCase):

    def test_capitalize_one_word(self):
        """
        Tests capitalize function with a single word
        :return: True if the result is expected value, False else
        """
        self.assertEqual(strings.capitalize("python"), "Python")

    def test_multiple_words(self):
        """
        Tests capitalize function with multiple words
        :return:
        """
        self.assertEqual(strings.capitalize("python is genial"), "Python is genial")


if __name__ == '__main__':
    unittest.main()
