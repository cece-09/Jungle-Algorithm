import sys
T = int(input())
K = int(input())

coins = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]

DP = [0]*(T+1)
DP[0] = 1

for i in range(0, K):
    coin, cnt = coins[i]
    for money in range(T, -1, -1):

        # 동전이 지폐보다 크면 pass
        if money < coin:
            continue

        # 이 동전을 사용했다고 했을 때,
        # 남은 금액을 만드는 가짓수는
        for k in range(1, cnt+1):  # k는 쓴 횟수
            if coin * k > money:
                break

            left = money-coin*k
            DP[money] += DP[left]

print(DP[-1])
