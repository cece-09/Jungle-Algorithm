
s1 = input().strip()
s2 = input().strip()

N = max(len(s1), len(s2))
DP = [[0]*(N+1) for _ in range(N+1)]

S1 = []
S2 = []

# 문자열 가공 (길이를 같게)
for i in range(N):
    if i < len(s1):
        S1.append(s1[i])
    else:
        S1 = ['0'] + S1

for i in range(N):
    if i < len(s2):
        S2.append(s2[i])
    else:
        S2 = ['0'] + S2

# 2차원 배열 돌면서 LCS 저장
# DP[i][j] S1[:i], S2[:j]의 LCS
for i in range(1, N+1):
    for j in range(1, N+1):
        DP[i][j] = max(DP[i-1][j], DP[i][j-1])

        if S1[j-1] == S2[i-1]:
            DP[i][j] = DP[i-1][j-1]+1


print(DP[N][N])
print(DP)
