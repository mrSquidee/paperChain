import random
from collections import Counter

fun = [lambda a,b: a & b] + \
    [lambda a,b: a | b] + \
    [lambda a,b: a ^ b]

def cepic(m):
    n = 8
    m = [m[i:i+n] for i in range(0, len(m), n)] # chuncc
    print(m)
    e=[]

    for i in range(8):
        b = 0
        for j in range(7):
            b += int(m[j][i])
        e.append(b**2)

    for i in range(8): # mini bepic
        w = int(str(e[i])[-1]) + e[i] + i + 2
        e[i] = int(str(w)[0]) * w * (i+1)

    inter = 0
    final = ''
    for i in range(8):
        nextBit = str(((inter >> i) ^ (e[i] << i)) % 10)
        final += nextBit
        inter = e[i]
    return int(final)

# for i in range(1000000):
#     m = ''.join(str(random.randint(0,9)) for _ in range(56))

c = []

for i in range(10):
    m = '0'*55 + str(i)
    print(m, cepic(m))

# cols = 0
# count = Counter(c)
# for i in count:
#    cols += count[i] - 1

# print(cols)