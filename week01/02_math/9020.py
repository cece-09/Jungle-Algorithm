import sys
T = int(input())


def is_prime(N):
    if N == 2:
        return True
    if N == 1:
        return False
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            return False
    return True


for _ in range(T):
    case = int(input())
    for i in range(case//2, 1, -1):
        if is_prime(i) and is_prime(case-i):
            print("{} {}".format(min(i, case-i), max(i, case-i)))
            break
