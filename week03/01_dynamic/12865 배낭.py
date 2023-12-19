import sys

N, K = map(int, input().split())
stuff = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [[0]*(K+1) for _ in range(N+1)]

stuff.sort()
for i in range(1, N+1):
    weight, cost = stuff[i-1]
    for j in range(K+1):
        if weight <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-weight]+cost)
        else:
            DP[i][j] = DP[i-1][j]


print(DP[-1][K])
