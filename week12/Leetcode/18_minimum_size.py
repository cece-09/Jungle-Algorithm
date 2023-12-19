class Solution(object):
    def minSubArrayLen(self, target, nums):
        # Returns if size-length subarray
        # whose sum is equal to target exists in array
        def ge_target(nums, size, n, target):
            s, e = 0, size-1
            nsum = sum(nums[0:size])
            while True:
                if nsum >= target:
                    return True
                
                if e+1 >= n:
                    break
                nsum -= nums[s]
                nsum += nums[e+1]
                e += 1
                s += 1
                
            return False
        
        # Do binary search to find return value
        def binary_search(nums, target, n, lo, hi):
            while lo+1 < hi:
                mid = (lo+hi)//2
                if ge_target(nums, mid, n, target):
                    hi = mid
                else:
                    lo = mid
            return hi

        # Main 
        n = len(nums)
        lo, hi = 1, n

        # Handle exceptions first
        if ge_target(nums, lo, n, target):
           return 1

        if not ge_target(nums, hi, n, target):
           return 0 
        
        # Return the result of binary search
        return binary_search(nums, target, n, lo, hi)


sol = Solution()
sol.minSubArrayLen(11, [1,2,3,4,5])