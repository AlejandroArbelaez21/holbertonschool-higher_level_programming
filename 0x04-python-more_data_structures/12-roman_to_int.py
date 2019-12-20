#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string):
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for x, y in my_dict.items():
            if my_dict[x] == roman_string:
                sum = sum + my_dict[y]
        return (sum)
    return(0)    
