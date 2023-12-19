class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # n번째 계단을 오르는 가짓수
        dp = [0 for _ in range(n+1)]

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
        

sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))