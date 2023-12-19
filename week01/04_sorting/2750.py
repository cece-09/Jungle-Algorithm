# QuickSort
import sys
sys.setrecursionlimit(10**4)


def partition(s, e):
    pivot = nums[s]
    p = s
    j = s  # pivot 위치
    for i in range(s+1, e):
        if nums[i] < pivot:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[j], nums[p] = nums[p], nums[j]
    return j


def quick_sort(s, e):
    if s < e-1:
        # pivot 설정
        pivot = partition(s, e)
        quick_sort(s, pivot)
        quick_sort(pivot+1, e)
    else:
        return


N = int(input())
nums = [int(input()) for _ in range(N)]

quick_sort(0, len(nums))

for num in nums:
    print(num)
