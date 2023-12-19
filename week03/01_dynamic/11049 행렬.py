import sys
N = int(input())
mtx = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

inf = float('inf')
DP = [[0]*N for _ in range(N)]

for i in range(N):
    DP[i][i] = 0

for diagonal in range(1, N):
    for i in range(N-diagonal):
        j = i+diagonal

        DP[i][j] = inf
        for k in range(i, j):
            mul = mtx[i][0]*mtx[k][1]*mtx[j][1]
            DP[i][j] = min(DP[i][j], DP[i][k]+DP[k+1][j] + mul)

print(DP[0][N-1])
