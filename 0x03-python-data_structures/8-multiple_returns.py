#!/usr/bin/python3
def multiple_returns(sentence):
    while (sentence):
        if sentence == "":
            sentence = "None"
        if sentence == " ":
            sentence = "None"
    return (len(sentence), sentence[0])
