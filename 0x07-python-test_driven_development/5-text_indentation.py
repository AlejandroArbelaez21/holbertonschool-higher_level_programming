#!/usr/bin/python3
def text_indentation(text):
    if (text):
        if type(text) is not str:
            raise TypeError("text must be a string")
        else:
            for x in range(len(text)):
                if text[x] == "." or text[x] == "?" or text[x] == ":":
                    print(text[x])
                    print()
                else:
                    print(text[x], end="")
            print()
