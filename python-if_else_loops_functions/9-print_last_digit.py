#!/usr/bin/python3
def print_last_digit(number):
    # abs / absolute value of a number without regard to + or -
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
