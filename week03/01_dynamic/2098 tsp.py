import sys


def tsp(curr, visit):
    if visit == (1 << N)-1:  # if all visited
        if W[curr][0] == 0:
            return inf
        return W[curr][0]

    if DP[curr][visit] != -1:
        # 도시가 4개 이하이면 이 블록으로 진입 x
        return DP[curr][visit]

    DP[curr][visit] = inf

    for i in range(N):
        if W[curr][i] == 0:
            continue  # 경로 없음
        if (visit & (1 << i)) != 0:
            continue  # 이미 방문
        DP[curr][visit] = min(DP[curr][visit], W[curr]
                              [i]+tsp(i, visit | 1 << i))  # visit

    return DP[curr][visit]


N = int(input())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


inf = float('inf')
DP = [[-1]*(1 << N) for _ in range(N)]

print(tsp(0, 1))
