
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [0 for _ in range(M+1)]

weight, value = [], []

for _ in range(N):
    V, C, K = map(int, input().split())  # 무게, 가치, 개수

    idx = 1
    while K > 0:
        tmp = min(idx, K)

        weight.append(V*tmp)
        value.append(C*tmp)

        K -= tmp
        idx *= 2


for i in range(len(weight)):
    now_w = weight[i]
    now_v = value[i]

    for j in range(M, now_w-1, -1):
        dp[j] = max(dp[j], dp[j-now_w] + now_v)

print(dp[M])
