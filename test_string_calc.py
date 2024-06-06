import unittest
from string_calc import add_string


class TestStringCalc(unittest.TestCase):

    def test_empty_string(self):
        result = add_string("")
        self.assertEqual(result, 0)

    def test_one_number_in_string(self):
        result = add_string("1")
        self.assertEqual(result, 1)

    def test_two_numbers_in_string(self):
        result = add_string("1,5")
        self.assertEqual(result, 6)

    def test_any_amount_of_numbers(self):
        result = add_string("1,2,3,4,5")
        self.assertEqual(result, 15)

    def test_new_line_delimiter(self):
        result = add_string("1\n2,3")
        self.assertEqual(result, 6)

    def test_dynamic_delim(self):
        result = add_string("//;\n1;2")
        self.assertEqual(result, 3)

    def test_one_negative_number_in_string(self):
        with self.assertRaisesRegex(ValueError, "Negatives not allowed: <-2>"):
            add_string("1,-2")

    def test_negative_numbers_in_string(self):
        with self.assertRaisesRegex(ValueError, "Negatives not allowed: <-2, -4>"):
            add_string("1,-2, 3, -4")

    def test_delim_asterix_multiplies(self):
        result = add_string(("//*\n2*8"))
        self.assertEqual(result, 16)


if __name__ == "__main__":
    unittest.main()
