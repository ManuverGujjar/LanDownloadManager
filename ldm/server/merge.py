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

from ldm.config import MEDIA_DIR
from ldm.config import FILE_NAME

import os

with open(os.path.join(MEDIA_DIR, FILE_NAME), 'wb') as file:
    for i, j in parts:
        f2 = open(os.path.join(MEDIA_DIR, f'{i}'), 'rb')
        file.write(f2.read())


