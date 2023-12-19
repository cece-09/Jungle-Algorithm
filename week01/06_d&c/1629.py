import sys
sys.setrecursionlimit(10**8)

A, B, C = list(map(int, input().split()))


def modulo(n):
    if n == 1:
        return (A % C)

    tmp = modulo(n//2)
    if n % 2 == 0:
        return tmp * tmp % C
    return A * tmp * tmp % C


print(modulo(B))
