import unittest
from milestone09 import Add


class TestAddMethods(unittest.TestCase):

    def test_empty_string(self):
        actual = Add('')
        self.assertEqual(actual, 0)

    def test_one_digit_number(self):
        actual = Add('1')
        self.assertEqual(actual, 1)

    def test_two_digit_number(self):
        actual = Add('13')
        self.assertEqual(actual, 13)

    def test_two_numbers_with_one_digit(self):
        actual = Add('1,2')
        self.assertEqual(actual, 3)

    def test_two_numbers_with_multiple_digits(self):
        actual = Add('1,12,345')
        self.assertEqual(actual, 358)

    def test_handling_new_lines_between_numbers_if_comma(self):
        actual = Add('1,\n')
        self.assertEqual(actual, 'WRONG INPUT')


if __name__ == "__main__":
    unittest.main()
