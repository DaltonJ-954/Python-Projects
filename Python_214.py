import os

import time

fname1 = 'lion.txt'

fname2 = 'elephant.txt'

fpath = 'C:\\techKnowledgey\\'
the_absolute = os.path.join(fpath, fname1, fname2)
print(the_absolute)

listed = os.listdir(r'C:\\techKnowledgey\\')
print(listed)

print(time.ctime(time.time()))

