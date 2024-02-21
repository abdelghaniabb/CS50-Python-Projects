#!/usr/bin/python3

# https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias
import emoji

user_input = input('Input: ')
print('Output:', emoji.emojize(user_input, language='alias'))
