import sys

# attackable 함수 구간 (s, e)에 배열m의 값이 존재하는지 확인


def attackable3(x, y):  # simple for문 O(L)
    s, e = x-(L-y), x+(L-y)
    for i in range(s, e+1):
        if i in m:
            return True
    return False


def attackable2(x, y):  # two pointer O(M)
    s, e = x-(L-y), x+(L-y)
    # 만약 s == e 이면 이 x좌표에 사대가 있는지만 검사
    if s == e:
        return s in m
    i, j, k = 0, M-1, 0
    # two pointer로 m[i] < s 이거나 m[i] > e 인 인덱스 검색
    while k < M:
        if m[i] < s:
            i += 1
        if m[j] > e:
            j -= 1
        if i >= j:
            break
        k += 1
    if i > j:
        return False
    if i == j:
        if i == s or i == e:
            return False
        # 만난 값이 (s, e)에 속하는지 반환
        return s <= m[i] <= e
    return True


def attackable(x, y):  # binary search O(logM)
    s, e = x-(L-y), x+(L-y)
    # 검사할 필요가 없는 경우
    if m[-1] < s or m[0] > e:
        return False

    # 만약 s = e이면 이 점이 사대인지만 확인
    if s == e:
        return s in m

    v1, v2 = 0, M-1
    if m[0] >= s:
        # 만약 첫번재 원소가 s보다 >=, 모든 원소가 s보다 >= (all T)
        v1 = 0
    else:
        # m[i] >= s 인 최소의 값 v1 탐색: lower bound
        # s보다 크거나 같은 수가 처음 등장하는 위치를 찾는다
        low, high = 0, M-1
        while low+1 < high:  # low와 high 사이에는 한 칸 존재
            mid = (low+high)//2
            if m[mid] >= s:  # if true
                high = mid
            else:
                low = mid
        v1 = high

    if m[-1] <= e:
        # 만약 마지막 원소가 e보다 <=, 모든 원소가 e보다 <= (all F)
        v2 = M-1
    else:
        # m[i] > e 인 최소의 값 v2 탐색: upper bound
        # e보다 큰 수가 처음 등장하는 위치를 찾는다
        # 찾은 후 high-1 하면 e보다 작거나 같은 수의 최대 인덱스가 된다
        low, high = 0, M-1
        while low+1 < high:
            mid = (low+high)//2
            if m[mid] > e:  # if true
                high = mid
            else:
                low = mid
        v2 = high-1

    # 만약 v1 > v2라면 범위는 없다
    if v1 > v2:
        return False
    return True


M, N, L = map(int, input().split())
m = list(map(int, input().split()))
n = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


m.sort()
lower = m[0]-L
upper = m[-1]-L

excp = 0
# y좌표가 L을 초과하면 제외하고
# 모든 점에 대해 사정거리 안에 있는지 여부 조사
for i in range(N):
    if n[i][1] > L:
        excp += 1
        continue
    if not attackable(n[i][0], n[i][1]):
        excp += 1

print(N-excp)
