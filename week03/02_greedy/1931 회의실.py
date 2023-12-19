import sys

N = int(input())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# sort by end time
# choose the shortest
meetings.sort(key=lambda m: (m[1], m[0]))

tmp = 0
cnt = 0
for s, e in meetings:
    if s >= tmp:
        cnt += 1
        tmp = e

print(cnt)
