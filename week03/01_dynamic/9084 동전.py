import sys


TC = int(input())

for _ in range(TC):
    N = int(input())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(input())

    DP = [0]*(M+1)
    DP[0] = 1

    for i in range(N):
        coin = coins[i]
        for j in range(M+1):
            if j < coin:
                continue
            left = (j-coin)
            DP[j] += DP[left]  # coin을 몇 개 사용?

    print(DP[M])
