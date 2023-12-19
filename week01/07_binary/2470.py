import sys
N = int(input())
X = list(map(int, input().split()))
X.sort()

# ? binary search
sum = float('inf')
answer = [-1, -1]
for i in range(N):
    s, e = i+1, N-1
    j = i
    # X[i]와 더해서 0과 가장 가까이가는 수 찾기
    # -X[i]보다 큰 최소의 수를 찾는다
    if X[s] > -X[i]:
        j = s
    elif X[e] < X[i]:
        j = e
    else:
        while s+1 < e:
            mid = (s+e)//2
            if X[mid] > -X[i]:
                e = mid
            else:
                s = mid
                j = mid if j == i or abs(X[i]+X[mid]) > abs(X[i]+X[j]) else j
    # mid, mid+1에 대해 체크
    # j = mid-1 if abs(X[i]+X[mid]) > abs(X[i]+X[mid-1]) else mid
    if abs(X[i]+X[j]) < sum:
        sum = X[i]+X[j]
        answer = [X[i], X[j]]


# two pointer
# left/right 사이드의 가장 안쪽 -><- 값을 찾음
i, j = 0, N-1
sum = X[i] + X[j]
answer = [X[i], X[j]]
while i < j:
    if abs(X[i] + X[j]) < abs(sum):
        sum = X[i] + X[j]
        answer[0], answer[1] = X[i], X[j]
        if sum == 0:
            break
    if X[i] + X[j] < 0:
        i += 1
    else:
        j -= 1


print(answer[0])
print(answer[1])
