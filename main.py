from itertools import product

count = 0
for i in product(("СТЁПА"), repeat=4):
    if i.count('Ё') == 1:
        count += 1

print(count)