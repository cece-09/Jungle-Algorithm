import sys
N, K = map(int, input().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
count = [0] * N
coins.sort(reverse=True)

total_cnt = 0
for i in range(N):
    while coins[i] <= K:
        count[i] += 1
        total_cnt += 1
        K -= coins[i]
    if K == 0:
        break

print(total_cnt)
