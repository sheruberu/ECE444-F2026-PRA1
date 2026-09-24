import unittest
from utils import utils


class TestReversed(unittest.TestCase):

    def test_reversed_with_integer(self):
        self.assertEqual(utils.reversed(123), 321)

    def test_reversed_with_negative_integer(self):
        self.assertEqual(utils.reversed(-123), -321)

    def test_reversed_with_string(self):
        with self.assertRaises(TypeError):
            utils.reversed("123")

    def test_reversed_with_float(self):
        with self.assertRaises(TypeError):
            utils.reversed(12.3)


class TestFormatter(unittest.TestCase):

    def test_formatter_with_integer(self):
        self.assertEqual(utils.formatter(8), ("1000", "10"))

    def test_formatter_with_string(self):
        with self.assertRaises(TypeError):
            utils.formatter("8")

    def test_formatter_with_float(self):
        with self.assertRaises(TypeError):
            utils.formatter(8.0)


if __name__ == "__main__":
    unittest.main()
