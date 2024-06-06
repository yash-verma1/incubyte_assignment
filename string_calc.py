import re
from functools import reduce

def add_string(string_to_calc):
    delim = [",", "\n"]
    if string_to_calc == "":
        # Returns 0 if empty string is passed
        return 0

    if string_to_calc.startswith("//"):
        # update the delimiter, its after `//` and before '\n'
        delim.append(re.escape(string_to_calc[2:3]))
        # Update the string_to_calc after the newline char
        string_to_calc = string_to_calc[4:]

    # string for regex to remove delimiters from string_to_calc
    delims = "|".join(delim)

    # generate a list of numbers after removing the delimite
    list_of_numbers = [
        int(num) for num in re.split(r"{}".format(delims), string_to_calc)
    ]

    # check if there are any negative numbers in the list
    negative_numbers = [str(x) for x in list_of_numbers if x < 0]

    if negative_numbers:  # throw an exception
        raise ValueError(
            "Negatives not allowed: <{}>".format(", ".join(negative_numbers))
        )
    
    if delim[-1] == re.escape('*'):
        return reduce(lambda x,y : x *y, list_of_numbers)

    return sum(list_of_numbers)
