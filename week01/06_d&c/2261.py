# Closest Pair
import sys
import math


def distance(d1: tuple, d2: tuple):  # 거리 제곱
    return (d1[0]-d2[0])**2 + (d1[1]-d2[1])**2


def closest_pair(s, e):
    global minD
    if e - s == 1:
        return
    if e - s == 2:
        d = distance(D[s], D[e-1])
        if minD == None or minD > d:
            minD = d
        return

    # x좌표의 mid값 구하기
    mid = (s + e) // 2

    closest_pair(s, mid)
    closest_pair(mid, e)
    d = minD

    # mid-d < x < mid+d 점 (중간 영역) 조사
    for i in range(mid, s-1, -1):
        if D[mid][0] - D[i][0] > math.sqrt(d):
            break
    for j in range(mid, e):
        if D[j][0] - D[mid][0] > math.sqrt(d):
            break

    # i~j 중간 영역에서의 최근접점 조사
    mids = sorted(D[i:j+1], key=lambda d: d[1])
    for p in range(len(mids)-1):
        for q in range(p+1, len(mids)):
            if mids[q][1] - mids[p][1] >= math.sqrt(d):
                break
            minD = min(minD, distance(mids[q], mids[p]))

    return


# 입력을 받음
N = int(input())
D = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
minD = None

# D배열의 x좌표값을 기준으로 정렬
D.sort(key=lambda d: d[0])

# 재귀 호출
closest_pair(0, N)
print(minD)
