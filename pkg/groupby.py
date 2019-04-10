import os.path
from itertools import groupby
numbers = [10, 13, 16, 22, 9, 4 , 37]
d = {'even':[], 'odd':[]}
for k,g in groupby(numbers, lambda x: x % 2):
        if k:
            d['odd'].extend(g)
        else:
            d['even'].extend(g)
print(d)
path=input(" enter the path\n")
for path,subdir,files in os.walk(path):
   for x in subdir:
       print(os.path.join(path,x)) # will print path of directories
   for x in files:
       print(os.path.join(path,x)) #