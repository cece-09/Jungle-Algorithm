def cut(height: int):
    i = len(T)-1
    trees = 0
    for i in range(len(T)-1, -1, -1):
        if T[i] <= height:
            break
        trees += (T[i] - height)
    return trees


def binary_search(h: int):
    s, e = 0, h
    while s < e:
        if e-s <= 1:
            return s

        mid = (s + e) // 2
        trees = cut(mid)

        if trees == M:
            return mid
        if trees > M:
            s = mid
        else:
            e = mid


N, M = map(int, input().split())
T = list(map(int, input().split()))

# 나무를 높이순으로 정렬
T.sort()
max = T[-1]
H = binary_search(max)
print(H)
