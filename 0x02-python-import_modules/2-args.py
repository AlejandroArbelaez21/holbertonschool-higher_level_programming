#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("1 argument:")
        print("{}:".format(str(len(sys.argv) - 1)), sys.argv[1])
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print(str(len(sys.argv) - 1), "arguments:")
        for x in range(1, len(sys.argv)):
            print("{}:".format(x), sys.argv[x])
