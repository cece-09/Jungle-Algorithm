# Counting Sort
import sys
N = int(input())

C = [0] * 10000
for _ in range(N):
    num = int(sys.stdin.readline())
    C[num-1] += 1

for i in range(10000):
    for j in range(C[i]):
        print(i+1)
