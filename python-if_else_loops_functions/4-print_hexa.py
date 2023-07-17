#!/usr/bin/python3
# Print numbers Hexadecimal in string format
string = "{} = 0x{:x}"
for number in range(99):
    print(string.format(number, number))
