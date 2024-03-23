#!/usr/bin/python3

def main():
    user_input = input('Input: ')
    print('Output:', shorten(user_input))

def shorten(word):
    """omits all vowels from a string"""
    new_str = ''
    for char in word:
        if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_str += char
    return new_str


if __name__ == '__main__':
    main()


