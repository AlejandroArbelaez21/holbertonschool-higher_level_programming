#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 0
    if len(sys.argv) == 1:
        print(int(0))
    elif len(sys.argv) == 2:
        print(int(sys.argv[1]))
    else:
        for x in range(1, len(sys.argv)):
            i += int(sys.argv[x])
        print("{}".format(i))
