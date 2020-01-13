#!/usr/bin/python3
def text_indentation(text):
    if text:
        if type(text) is not str:
            raise TypeError("text must be a string")
        else:
            cont = 0
            sum = 0
            for y in range(len(text)):
                if text[y] == "." or text[y] == "?" or text[y] == ":":
                    sum += 1
            for x in range(len(text) - sum):
                if text[cont] == "." or text[cont] == "?" or text[cont] == ":":
                    print(text[cont])
                    print()
                    cont += 1
                    while text[cont] == " ":
                        cont += 1
                else:
                    print(text[cont], end="")
                    cont += 1
