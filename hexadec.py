import re

char_frequency = {}
cookie = input("Enter your cookie here:")

for c in cookie:
    if c in char_frequency:
        char_frequency[c] += 1
    else:
        char_frequency[c] = 1

for char, frequency in char_frequency.items():
    print("'{}' occurs {} times".format(char, frequency))

hex_pattern = re.compile(r'^[0-9a-fA-F]+$')

if hex_pattern.match(cookie):
    print("The input is a valid hexadecimal string.")
else:
    print("The input is not a valid hexadecimal string.")