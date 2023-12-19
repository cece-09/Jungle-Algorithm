import sys
N, M = map(int, input().split())
mtx = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# update first row
for i in range(1, M):
    mtx[0][i] += mtx[0][i-1]

# compare directions
for i in range(1, N):
    DP1 = mtx[i].copy()
    DP2 = mtx[i].copy()

    for j in range(M):
        if j == 0:  # 위에서 내려오는 경우
            DP1[j] += mtx[i-1][j]
        else:  # 위에서 내려오거나 왼쪽에서 오른쪽으로 가거나
            DP1[j] += max(mtx[i-1][j], DP1[j-1])

    for j in range(M-1, -1, -1):
        if j == M-1:  # 위에서 내려오는 경우
            DP2[j] += mtx[i-1][j]
        else:  # 위에서 내려오거나, 오른쪽에서 왼쪽으로 가거나
            DP2[j] += max(mtx[i-1][j], DP2[j+1])

    for k in range(M):
        mtx[i][k] = max(DP1[k], DP2[k])


print(mtx[N-1][M-1])
