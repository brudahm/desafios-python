#!/bin/python3
def numberOfPairs(ar, k):

    count = 0
    n = len(ar)

    if k == 0:
        raise ValueError("Nao e possivel dividir por zero")

    for i in range(n):

        for j in range(i+1, n):

            if (ar[i]+ar[j]) % k == 0:
                count += 1

    return count
