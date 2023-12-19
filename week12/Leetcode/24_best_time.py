class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
    
        k, profit = 0, 0
        for i in range(n):
            if prices[i] < prices[k]:
                k = i # update
            profit = max(profit, prices[i] - prices[k])

        return profit
        

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))