import sys

N, K = map(int, input().split())
stuff = []


# 물건을 분할한다
for _ in range(N):
    v, c, k = map(int, sys.stdin.readline().split())
    # k를 2의 거듭제곱으로 나누기
    idx = 1
    while k > 0:
        tmp = min(idx, k)  # idx는 2의 제곱수
        stuff.append((v*tmp, c*tmp))
        idx *= 2
        k -= tmp

# knapsack
N = len(stuff)
DP = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    v, c = stuff[i-1]
    for j in range(K+1):
        if v <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-v]+c)
        else:
            DP[i][j] = DP[i-1][j]


print(DP[-1][K])
