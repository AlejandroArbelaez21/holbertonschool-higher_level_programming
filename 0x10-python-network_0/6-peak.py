#!/usr/bin/python3
"""
This module contains find_peak funtion
"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    return find_peak(list_of_integers[1:-1])
