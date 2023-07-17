#!/usr/bin/python3
# :d / indicates 1-digit numbers without leading zeros
#      and without specific fields
numbers = "{:d}{:d}"
for num1 in range(9):
    for num2 in range(num1 + 1, 10):
        print(numbers.format(num1, num2), end="")
        if num1 != 8 or num2 != 9:
            print(", ", end="")
        else:
            print()
