#!/usr/bin/python3
"""
This module contains find_peak funtion
"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if list_of_integers == []:
        return None
    else:
        return max(list_of_integers)
