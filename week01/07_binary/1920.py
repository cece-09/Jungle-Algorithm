

def merge(A: list[int], B: list[int]) -> list[int]:
    i, j, k = 0, 0, 0
    m = len(A) + len(B)
    M = [0] * m
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            M[k] = A[i]
            i += 1
        else:
            M[k] = B[j]
            j += 1
        k += 1

    while k < m:
        if i >= len(A):
            M[k] = B[j]
            j += 1
        else:
            M[k] = A[i]
            i += 1
        k += 1
    return M


def merge_sort(arr: list[int], n: int) -> list[int]:
    if n == 1:
        return arr
    L = merge_sort(arr[:n//2], n//2)
    R = merge_sort(arr[n//2:], n - n//2)
    return merge(L, R)


def binary_search(key: int, arr: list[int]) -> bool:
    s, e = 0, len(arr)
    while s < e:
        m = (s + e) // 2
        if key == arr[m]:
            return True
        if e-s == 1:
            return False
        if key < arr[m]:
            e = m
        else:
            s = m
    return True


N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

# sort first
n = merge_sort(n, N)

# search
for i in range(M):
    rslt = binary_search(m[i], n)
    if rslt == True:
        print(1)
    else:
        print(0)
