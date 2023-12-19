
# ! 못 풀었습니다
import sys


def length(n, cnt):
    global k
    if cnt >= N:
        return cnt
    k += 1
    return length(n+1, cnt*2+n+1)


def solve(n, k, cnt):
    if k == 1:
        return 3
    tmp = solve(n, k-1, cnt)
    # if
    return tmp*2+k+3


N = int(input())
# moo(3, 0, [3])
k = 0
len = length(3, 0)
print(len, k)
answer = solve(N, k, 0)

print(answer)
