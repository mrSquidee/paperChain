from collections import Counter
import math

def split(m):
   h = math.floor(len(m)/2)
   s = [m[0:h], m[h:]]
   return s

def leftRotate(x, n): # input x as string
    out = x[n:] + x[:n]
    return int(out,2)

def rightRotate(x, n): # input x as string
    out = x[len(x)-n:] + x[:len(x)-n]
    return int(out,2)

def getint(m1, m2): # input strings
    i1 = m1.count('1')
    i2 = m2.count('0')
    return str(leftRotate(m1, i1) ^ rightRotate(m2, i2))[-1]

def depic(m):
    n = 8
    m = [m[i:i+n] for i in range(0, len(m), n)] # chuncc
    e = []

    for i in range(8): # split
        b = 0
        for j in range(7):
            b += int(m[j][i])
        e.append(b)

    b = 0
    for i in m[-1]: # sum nonce
        b += int(i)

    for i in range(8): # add stuff
        e[i] = e[i] + b + i + 1

    q = '' # convert to binary
    for i in e:
        q+=bin(i)[2:]

    final = ''

    final += str(int(q,2))[-2]

    layer1 = split(q)

    final += getint(layer1[0], layer1[1])

    layer2 = split(layer1[0]) + split(layer1[1]) + split(bin(int(layer1[0],2)^int(layer1[1],2))[2:])
    # print(layer1, layer2)

    combine = [[0, 1], [2, 3], [4, 5], [0, 3], [1, 4], [2, 5]]

    for i in combine:
        for j in range(2):
            if(layer2[i[j]]==''):
                layer2[i[j]] = '0'
        final += getint(layer2[i[0]], layer2[i[1]])

    return final