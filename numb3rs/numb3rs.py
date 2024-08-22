#!/usr/bin/python3

import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression to match a valid IPv4 address
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)

    if match:
        # Check each segment to ensure it's between 0 and 255
        for segment in match.groups():
            if int(segment) < 0 or int(segment) > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
