N = int(input())
X = list(map(int, input().split()))
DP = [0 for _ in range(N)]

DP[0] = 1
for i in range(N):
    DP[i] = 1
    for j in range(i):
        if X[j] < X[i]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))
