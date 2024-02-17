#!/usr/bin/python3

user_input = input('File name: ')

extension = user_input.split('.')[-1].lower().replace(' ', '')
if extension in ['jpg', 'jpeg']:
    print('image/jpeg')
elif extension in ['gif', 'png']:
    print('image/' + extension)
elif extension in ['pdf', 'zip']:
    print('application/' + extension)
elif extension == 'txt':
    print('text/plain')
else:
    print('application/octet-stream')
