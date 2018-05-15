import os

file = os.path.join('input.txt')

with open(file, 'r') as text:
    print(text)

    lines=text.read()

    print(lines)