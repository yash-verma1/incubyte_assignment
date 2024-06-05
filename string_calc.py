import unittest

def add_string(string_to_calc):
    if string_to_calc == '':
        """ Returns 0 if empty string is passed. """
        return 0
    # Breaks the string in to a list of stringified numbers, maps them into an object and converts them into int
    list_of_numbers = map(int, string_to_calc.split(','))
    
    return sum(list_of_numbers)
    

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

if __name__ == '__main__':
    unittest.main()