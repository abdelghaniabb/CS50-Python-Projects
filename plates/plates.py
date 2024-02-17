#!/usr/bin/python3

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not(s[0].isalpha() and s[1].isalpha()):
        return False
    for char in s:
        if not (char.isalpha() or char.isnumeric()):
            return False
    i = 0
    while i < len(s) and not s[i].isnumeric():
        i += 1
    if len(s) == i:
        return True

    if s[i] == '0':
        return False
    while i < len(s):
        if not s[i].isnumeric():
            return False
        i += 1
    return True


main()
