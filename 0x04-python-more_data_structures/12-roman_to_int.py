#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for x, y in dic.items():
            if dic[x] == roman_string:
                sum = sum + dic[y]
        return (sum)
    return(0)
