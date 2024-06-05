import unittest

def add_string(string_to_calc):
    if string_to_calc == '':
        """ Returns 0 if empty string is passed. """
        return 0
    pass

class TestStringCalc(unittest.TestCase):
    def test_empty_string(self):
        result = add_string("")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()