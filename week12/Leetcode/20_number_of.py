class Solution(object):
    def numIslands(self, grid):
        # Count the number of
        # connected components
        answer = 0
        direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        n = len(grid)     # row
        m = len(grid[0])  # col
        visit = [[0 for _ in range(m)] for _ in range(n)]
        dfsed = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(row, col):
            if dfsed[row][col]:
                # If dfsed before, return
                return False
            
            dfsed[row][col] = 1
            if grid[row][col] == "0":
                # If coord is sea, return
                return True
            
            for d in direc:
                r, c = row+d[0], col+d[1]
                if 0 <= r < n and 0 <= c < m and not visit[r][c]:
                    visit[r][c] = 1
                    dfs(r, c)
            return True


        for i in range(n):
            for j in range(m):
                # dfs grid if node is land
                if grid[i][j] == "1":
                    if dfs(i, j):
                        answer += 1

        return answer


        
sol = Solution()
sol.numIslands([["1","0","1","1","0","1","1"]])