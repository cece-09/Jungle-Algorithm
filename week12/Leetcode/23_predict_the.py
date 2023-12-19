class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)

        # dp[i][j]는 i to j 라운드에서
        # 첫 번째 플레이어와 두 번째 플레이어의 점수차
        dp = [[0 for _ in range(n)]]*n
        for i in range(n):
            dp[i][i] = nums[i]

        for k in range(1, n):
            for i in range(n-k):
                j = i+k
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        
        return dp[0][n-1] >= 0
        


sol = Solution()
print(sol.predictTheWinner([1,5,2]))
print(sol.predictTheWinner([1,5,233,7]))