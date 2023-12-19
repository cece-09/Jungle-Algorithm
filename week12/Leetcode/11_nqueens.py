class Solution(object):
    def totalNQueens(self, n):
        answer = 0
        def queen(k, i, x, y, z):
            nonlocal answer
            if i == k:
                answer += 1
                return
            
            for j in range(k):
                if j not in x and i+j not in y and i-j not in z:
                    queen(k, i+1, x+[j], y+[i+j], z+[i-j])
        
        queen(n, 0, [], [], [])
        return answer
                        

sol = Solution()
print(sol.totalNQueens(4))