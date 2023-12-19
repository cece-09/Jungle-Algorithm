# ! unsolved

import sys


N, M = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def print_map(mtx):
    for i in range(N):
        for j in range(M):
            print(mtx[i][j], end=' ')
        print()


DP = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]
direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

DP[0][0] = 1


def dfs(row, col):
    stack = []
    stack.append((row, col))

    while stack:
        row, col = stack.pop()

        # DP[row][col] = 1
        for dir in direc:
            nrow, ncol = row+dir[0], col+dir[1]
            if not (0 <= nrow < N and 0 <= ncol < M):
                # 범위가 아니면 패스
                continue

            if not visit[nrow][ncol]:
                visit[nrow][ncol] = 1
                stack.append((nrow, ncol))

            if maps[row][col] > maps[nrow][ncol]:
                # 다음 좌표의 높이가 지금보다 낮으면
                # 경로 수 갱신
                DP[nrow][ncol] += DP[row][col]


dfs(0, 0)
print_map(DP)
print(DP[N-1][M-1])
