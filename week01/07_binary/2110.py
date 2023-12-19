import sys

N, C = map(int, input().split())
X = [int(sys.stdin.readline()) for _ in range(N)]
X.sort()

upper = X[-1]-X[0]  # 현재 input에서 가능한 최대간격
lower = 1  # 현재 input에서 가능한 최소간격
s, e = lower, upper

while s <= e:
    mid = (s+e) // 2
    cnt = 1  # 첫 번째 집에 설치
    diff = upper
    # mid를 간격으로 하여 설치가능한 최대 수를 구한다
    curr = X[0]
    for i in range(1, N):
        if X[i]-curr >= mid:
            diff = min(diff, (X[i]-curr))  # n보다 크면서 최소인 간격
            cnt += 1
            curr = X[i]

    if cnt < C:
        e = mid-1  # 현재 간격으로는 모두 설치할 수 없음
    else:
        s = mid+1  # 공유기을 모두 설치가능함
        # 모두 설치 가능했을때의 거리가 현재까지 최대이면 update
        lower = max(lower, diff)

print(lower)
