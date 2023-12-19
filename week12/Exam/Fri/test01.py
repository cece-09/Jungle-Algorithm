# 2733

nums = [3,2,1,4]

def solution():
    n = len(nums)
    if n < 3:
        return -1
    
    # O(nlogn)
    nums.sort()

    # O(n)    
    min_, max_ = min(nums), max(nums)
    for i in range(n):
        if nums[i] != min_ and nums[i] != max_:
            return nums[i]

    # O(1)
    a, b, c = nums[0], nums[1], nums[2]
    if b > a > c or c > a > b:
        return a

    if a > b > c or c > b > a:
        return b
    
    if a > c > b or b > c > a:
        return c