from collections import deque
from heapq import heappop, heappush

inf = float('inf')
N, K = map(int, input().split())
dist = [inf for _ in range(100001)]
vist = [0 for _ in range(100001)]

S, D = N, K

# move = []
queue = []
heappush(queue, (0, S))
dist[S] = 0

while queue:
    d, u = heappop(queue)

    for v in [u-1, u+1, 2*u]:
        if 0 <= v < 100001:
            dist[v] = min(dist[v], dist[u]+1)
            if vist[v] == 0:
                heappush(queue, (dist[v], v))
                vist[v] = 1

print(dist[D])
