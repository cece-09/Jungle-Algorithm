import sys


def cuttable(x, y, n):
    sump = 0
    for i in range(y, y+n):
        sumr = sum(paper[i][x:x+n])
        if 0 < sumr < n:  # 만약 한 줄의 sum이 != 0 and < n 이면 바로 return false
            return -1
        sump += sum(paper[i][x:x+n])
    if sump == n**2:
        return 1
    if sump == 0:
        return 0
    return -1


def cut(x, y, n):
    if n == 1 or cuttable(x, y, n) > -1:
        c = cuttable(x, y, n)
        result[c] += 1
        return
    cut(x, y, n//2)
    cut(x, y+n//2, n//2)
    cut(x+n//2, y, n//2)
    cut(x+n//2, y+n//2, n//2)


N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0, 0]  # count 결과 저장

# 수행
cut(0, 0, N)
print(result[0])
print(result[1])
