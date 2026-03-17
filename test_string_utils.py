import unittest
from string_utils import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_sentence(self):
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("A"), "A")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            reverse_string(123)

if __name__ == "__main__":
    unittest.main()
