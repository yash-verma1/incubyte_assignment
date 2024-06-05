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

    # generate a list of numbers after removing the delimiters
    list_of_numbers = [int(num) for num in re.split(r'{}'.format(delims), string_to_calc)]
    
    # check if there are any negative numbers in the list
    negative_numbers = [str(x) for x in list_of_numbers if x < 0]

    if negative_numbers:    # throw an exception
        raise ValueError("Negatives not allowed: <{}>".format(', '.join(negative_numbers)))
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

    def test_one_negative_number_in_string(self):
        with self.assertRaisesRegex(ValueError, "Negatives not allowed: <-2>"):
            add_string("1,-2")

    def test_negative_numbers_in_string(self):
        with self.assertRaisesRegex(ValueError, "Negatives not allowed: <-2, -4>"):
            add_string("1,-2, 3, -4")


if __name__ == '__main__':
    unittest.main()