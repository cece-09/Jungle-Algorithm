import sys


def travel(n, cst):
    global min_cst
    # 이전 도시, 출발 도시
    p, s = S[n-1], S[0]
    if n == N:
        if cost[p][s] == 0:
            return
        cst += cost[p][s]  # 출발지로 돌아감
        if min_cst == 0 or cst < min_cst:
            min_cst = cst
        return
    for i in range(N):
        if i in S:  # 이미 방문
            continue
        if n > 0 and cost[p][i] == 0:  # 방문 불가 (cost == 0)
            continue
        S[n] = i
        travel(n+1, cst + cost[S[n-1]][i])
        S[n] = -1


N = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S = [-1 for _ in range(N)]  # flag 배열

min_cst = 0  # 최소 cost
travel(0, 0)
print(min_cst)
