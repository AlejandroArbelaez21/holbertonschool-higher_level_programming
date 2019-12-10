#!/usr/bin/python3
for x in range(1, 101):
    if x % 15 == 0:
        print("FizzBuzz ", end="")
        continue
    elif x % 3 == 0:
        print("Fizz ", end="")
        continue
    elif x % 5 == 0:
        print("Buzz ", end="")
        continue
    print(x, end=" ")
print()
