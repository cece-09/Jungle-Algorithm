
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)

        dp = [0 for _ in range(n)]
        dp[0] = 1
        
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)


sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([0,1,0,3,2,3]))
print(sol.lengthOfLIS([7,7,7,7,7,7,7]))
print(sol.lengthOfLIS([4,10,4,3,8,9]))