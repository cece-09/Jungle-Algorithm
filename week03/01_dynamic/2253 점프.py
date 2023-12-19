import sys

N, M = map(int, input().split())
# DP[i][j]는 i까지 j점프로 왔다고 했을 때, 최소의 점프 횟수
DP = [[float('inf')]*(int((2*N)**0.5)+2) for _ in range(N+1)]
blocked = set()

for _ in range(M):  # 못 가는 돌
    blocked.add(int(sys.stdin.readline()))

DP[1][0] = 0  # 1까지 0점프로 오는 최소는 0
for i in range(2, N+1):
    if i in blocked:
        continue
    for j in range(1, int((2*i)**0.5)+1):
        DP[i][j] = min(DP[i-j][j], DP[i-j][j+1], DP[i-j][j-1]) + 1


answer = min(DP[N])
if answer == float('inf'):
    print(-1)
else:
    print(answer)
