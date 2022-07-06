import unittest
from shapes import rectangle, triangle, trapeze


class ShapesTestCase(unittest.TestCase):
    def setUp(self):
        self.side_A = 6
        self.side_B = 5
        self.high_H = 4

    def test_rectangle_with_correct_values(self):
        result = rectangle(6, 5)
        self.assertEqual(result, 30)

    def test_rectangle_with_incorrect_values(self):
        # self.assertRaises(ValueError, rectangle, self.side_A, 'example string')
        with self.assertRaises(ValueError):
            rectangle(self.side_A, 'example string')

    def test_triangle_with_correct_values(self):
        result = triangle(6, 5)
        self.assertEqual(result, 15)

    def test_triangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            triangle(self.side_A, 'example')

    def test_trapeze_with_correct_values(self):
        result = trapeze(self.side_A, self.side_B, self.high_H)
        self.assertEqual(result, 22)

    def test_trapeze_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            trapeze(self.side_A, self.side_B, 'example')

    def tearDown(self):
        del self.side_A
        del self.side_B


if __name__ == "__main__":
    unittest.main()
