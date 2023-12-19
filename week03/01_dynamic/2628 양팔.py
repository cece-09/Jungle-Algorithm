N = int(input())
weights = list(map(int, input().split()))

M = int(input())
marbles = list(map(int, input().split()))

MAX_WEIGHT = N*500 + 1
DP = [[0]*MAX_WEIGHT for _ in range(N)]

for i in range(N):
    weight = weights[i]  # 사용하는 추
    for now in range(1, MAX_WEIGHT):
        if now == weight:  # 현재 무게와 추의 무게 비교
            DP[i][now] = 1

        diff = abs(now-weight)
        plus = now+weight

        if diff > 0 and i > 0:
            DP[i][now] = max(DP[i-1][now], DP[i-1][diff])
        if plus < MAX_WEIGHT:
            DP[i][now] = max(DP[i][now], DP[i-1][plus])

for marble in marbles:
    if marble > N*500+1:
        print('N', end=' ')
    elif DP[-1][marble] > 0:
        print('Y', end=' ')
    else:
        print('N', end=' ')
print()
