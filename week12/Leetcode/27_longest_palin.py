class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        answer = [0, 0]
        # diff is 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                answer[0] = i
                answer[1] = i+1
        
        # diff is more than 2
        for diff in range(2, n):
            for i in range(n - diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    answer[0] = i
                    answer[1] = j
        

        i, j = answer[0], answer[1]
        return s[i:j+1]
                


sol = Solution()
# print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("ccc"))
