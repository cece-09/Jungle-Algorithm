import sys

# TODO 필요없는 case 지우기


def upper(k):  # k보다 큰 최소의 인덱스를 찾는다
    if dot[0] > k:
        return 0
    if dot[-1] <= k:
        return N
    s, e = 0, N-1

    while s+1 < e:
        m = (s+e) // 2
        if dot[m] > k:
            e = m
        else:
            s = m
    return e


def lower(k):  # k보다 크거나 같은 최소의 인덱스를 찾는다
    if dot[0] >= k:
        return 0
    if dot[-1] < k:
        return N-1
    s, e = 0, N-1

    while s+1 < e:
        m = (s+e) // 2
        if dot[m] >= k:
            e = m
        else:
            s = m
    return e


N, M = map(int, input().split())
dot = list(map(int, input().split()))
line = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dot.sort()

for i in range(M):
    s, e = line[i][0], line[i][1]
    if s > dot[-1] or e < dot[0]:
        print(0)
        continue
    v1 = lower(s)
    v2 = upper(e)
    print(v2-v1)
