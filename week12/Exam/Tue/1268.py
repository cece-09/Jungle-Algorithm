# Trie?

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        def lcs(s1, s2):
            n1 = len(s1)
            n2 = len(s2)
            dp = [[0 for _ in range(n1)] for _ in range(n2)]

            # dp[i][j]는 i부터 j까지의 최장공통부분문자열


        n = len(products)

sol = Solution()
print(sol.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))