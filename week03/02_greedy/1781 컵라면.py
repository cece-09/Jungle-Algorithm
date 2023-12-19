import sys
from heapq import heappop, heappush

N = int(input())

probs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# deadline 빠른순 정렬
probs.sort()


'''
1. 문제를 큐에 담음
2. 만약 큐의 길이가 현재 데드라인보다 길어지면
3. 큐에서 POP

선택된 문제를 데드라인 내료 풀 수 있음을 유지하면서
데드라인이 같고 리워드가 적은 문제를 빼냄 (Min heap)
'''

pq = []

for i in range(N):
    dead, cups = probs[i]
    heappush(pq, cups)
    if len(pq) > dead:
        heappop(pq)

print(sum(pq))
