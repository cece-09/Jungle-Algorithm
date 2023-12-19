S = input().strip()
N = len(S)

DP = [[0]*(N+1) for _ in range(N+1)]


for i in range(1, N+1):
    DP[i][i] = 1


for e in range(1, N+1):
    for s in range(1, N+1):
        if e < s:
            DP[e][s] = 1
        elif S[s-1] == S[e-1] and e-1 >= 0 and s+1 <= N:
            if DP[e-1][s+1] > 0:
                DP[e][s] = 1

# 분할 개수 구하기
inf = float('inf')
P = [inf for _ in range(N+1)]
P[0] = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if DP[j][i] > 0:  # if palindrome,
            P[j] = min(P[j], P[i-1]+1)

print(P[-1])
