import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    # ✅ Normal Cases
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    # ✅ Edge Cases
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 10), 0)

    def test_divide_float(self):
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)

    # ✅ Error Cases
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
