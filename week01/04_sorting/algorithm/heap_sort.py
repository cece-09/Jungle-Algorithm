# Heap Sort
import sys


def heapify(r, n):
    root = nums[r]
    k = r*2+1
    while k < n:
        k = k+1 if k+1 < n and nums[k+1] > nums[k] else k
        if root > nums[k]:
            return
        nums[(k-1)//2] = nums[k]
        k = k*2+1
    nums[k//2] = root


def heap_sort():
    # 배열의 처음 상태를 힙으로 만들기
    for i in range(len(nums)//2, -1, -1):
        heapify(i, len(nums))
    # 루트 노드를 꺼내 엔드 노드와 교환합니다.
    for i in range(len(nums)):
        nums[len(nums)-1-i], nums[0] = nums[0], nums[len(nums)-1-i]
        heapify(0, len(nums)-i-1)
    return


N = int(input())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# nums = [0, 45, 72, 13, 10002, 3]

heap_sort()
# print(nums)
for num in nums:
    print(num)
