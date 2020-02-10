parts = []

with open('parts.txt', 'r') as f:
    try:
        while True:
            line = f.readline()
            crange = line.split('-')
            parts.append((int(crange[0]), int(crange[1])))
    except:
        pass

print(parts)

DIR = 'PDClient'
FILE_NAME = 'Python Essential Reference.pdf'

import os

with open(FILE_NAME, 'wb') as file:
    for i, j in parts:
        f2 = open(os.path.join('..', DIR, f'{i}'), 'rb')
        file.write(f2.read())


