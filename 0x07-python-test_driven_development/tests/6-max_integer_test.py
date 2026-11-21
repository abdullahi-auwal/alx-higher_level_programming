import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([2, 4, 5]), 5)

    def test_all_negative(self):
        self.assertEqual(max_integer([-3, -6, -9]), -3)

    def test_all_zeros(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 5, 4]), 10)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([5, 10, 4]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([2.3, 5.4, 20.4]), 20.4)

    def test_None(self):
        with self.assertRaises(TypeError):
            max_integer(None)
