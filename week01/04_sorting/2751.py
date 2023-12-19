# Merge Sort

import sys
sys.setrecursionlimit(10**4)


def merge(s, m, e):
    global nums
    i = s
    j = m+1
    k = 0
    merged = nums[s:e+1]

    while i <= m and j <= e:
        if nums[i] < nums[j]:
            merged[k] = nums[i]
            i += 1
        else:
            merged[k] = nums[j]
            j += 1
        k += 1

    while k < e-s+1:
        if j > e:
            merged[k] = nums[i]
            i += 1
        else:
            merged[k] = nums[j]
            j += 1
        k += 1
    # merged -> nums
    nums[s:e+1] = merged


def merge_sort(s, e):
    if s < e:
        m = (s+e) // 2
        merge_sort(s, m)
        merge_sort(m+1, e)
        if nums[m] > nums[m+1]:
            merge(s, m, e)
    else:
        return


N = int(input())
nums = [int(sys.stdin.readline()) for _ in range(N)]

merge_sort(0, len(nums)-1)

for num in nums:
    print(num)
