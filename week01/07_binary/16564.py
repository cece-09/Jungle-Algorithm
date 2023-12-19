import sys

N, K = map(int, input().split())
X = sorted([int(sys.stdin.readline()) for _ in range(N)])

B = sum(X) + K
s, e = X[0], B

answer = X[0]
while s <= e:
    mid = (s+e) // 2

    # Xi가 mid보다 작은 경우 차를 합산
    dsum = 0
    for i in range(N):
        diff = X[i]-mid
        if diff < 0:
            dsum += -diff

    if dsum < K:
        s = mid+1
        answer = max(answer, mid)
    elif dsum > K:
        e = mid-1
    else:
        answer = max(answer, mid)
        break  # dsum == K
print(answer)
