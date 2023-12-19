'''
팰린드롬은 토마토 기러기 우영우
'''
import sys
N = int(input())
nums = list(map(int, input().split()))

M = int(input())
ques = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

DP = [[0]*(N) for _ in range(N)]

for i in range(N):
    DP[i][i] = 1

for e in range(N):
    for s in range(N):
        if e <= s:  # start > end
            DP[e][s] = 1  # consider 2*2 matrix
            continue
        if nums[s] == nums[e]:
            if s+1 < N and e-1 >= 0 and DP[e-1][s+1] > 0:
                DP[e][s] = 1

for s, e in ques:
    if DP[e-1][s-1] > 0:
        print(1)
    else:
        print(0)
