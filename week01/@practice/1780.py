# 재귀: 1780 종이의 개수
import sys


def cuttable(n, i, j):
    if n == 1:
        return mtx[i][j]
    paper = mtx[i][j]
    for k in range(i, i+n):
        for p in range(j, j+n):
            if mtx[k][p] != paper:
                return None
    return paper


def cut(n, i, j):  # i열 j행
    result = cuttable(n, i, j)
    if result != None:
        answer[result+1] += 1
        return
    n //= 3
    cut(n, i, j)
    cut(n, i+n, j)
    cut(n, i+2*n, j)
    cut(n, i, j+n)
    cut(n, i+n, j+n)
    cut(n, i+2*n, j+n)
    cut(n, i, j+2*n)
    cut(n, i+n, j+2*n)
    cut(n, i+2*n, j+2*n)


N = int(input())
mtx = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = [0, 0, 0]
cut(N, 0, 0)
print(answer[0])
print(answer[1])
print(answer[2])
