# 돌려볼 것

N = 50
DP = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N)]

for a in range(50):
    for b in range(50):
        for c in range(50):
            if a <= 0 or b <= 0 or c <= 0:
                DP[a][b][c] = 1

            elif a > 20 or b > 20 or c > 20:
                DP[a][b][c] = 20
                # DP[(a, b, c)] = DP[(20, 20, 20)]

            elif a < b and b < c:
                DP[a][b][c] = DP[a][b][c-1]+DP[a][b-1][c-1]-DP[a][b-1][c]

            else:
                DP[a][b][c] = DP[a-1][b][c]+DP[a-1][b-1][c] + \
                    DP[a-1][b][c-1]-DP[a-1][b-1][c-1]
