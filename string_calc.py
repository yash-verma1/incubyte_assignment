import re
import unittest

def add_string(string_to_calc):
    delim = [',', '\n']
    if string_to_calc == '':
        """ Returns 0 if empty string is passed. """
        return 0
    
    if string_to_calc.startswith('//'):
        # update the delimiter, its after `//` and before '\n'
        delim.append(string_to_calc[2:3])
        # Update the string_to_calc after the newline char
        string_to_calc = string_to_calc[4:]
     
    # string for regex to remove delimiters from string_to_calc
    delims = '|'.join(delim)

    # split the string_to_calc based on the delimiters
    list_of_numbers = map(int, re.split(r'{}'.format(delims), string_to_calc))
    
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

    def test_new_line_delimiter(self):
        result = add_string("1\n2,3")
        self.assertEqual(result, 6)

    def test_dynamic_delim(self):
        result = add_string("//;\n1;2")
        self.assertEqual(result, 3)    


if __name__ == '__main__':
    unittest.main()