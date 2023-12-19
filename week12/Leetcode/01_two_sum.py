# Leetcode https://leetcode.com/problems/two-sum
# target - nums[i]를 binary search로 찾는다.
# 이를 위해 idx array를 따로 만들어 둔다.

# 검색 시간을 줄이기 위해 hashmap을 쓸 수도 있다. (see editorial)

nums = [2,7,11,15]
target = 9

N = len(nums)
idx = [i for i in range(N)]
idx.sort(key=lambda x: nums[x])

def solution():
    for i in range(N):
        low = i+1
        hig = N-1

        diff = target - nums[idx[i]]
        
        # exception
        if nums[idx[hig]] == diff:
            return [idx[i], idx[hig]]
        
        if nums[idx[low]] == diff:
            return [idx[i], idx[low]]

        if nums[idx[hig]] < diff:
            continue

        if nums[idx[low]] > diff:
            continue

        # do binary search
        while low+1 < hig:
            mid = (low+hig)//2

            if nums[idx[mid]] < diff:
                low = mid  # false
            else:
                hig = mid  # true

        if nums[idx[hig]] == diff:
            return [idx[i], idx[hig]]
        
    return []


print(solution())
