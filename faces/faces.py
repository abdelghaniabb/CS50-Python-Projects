#!/usr/bin/python3

def convert(passed_str):
    """convert emoticons to emoji"""
    return passed_str.replace(':)', '🙂').replace(':(', '🙁')


def main():
    """this is the main function"""
    print(convert(input()))


main()
