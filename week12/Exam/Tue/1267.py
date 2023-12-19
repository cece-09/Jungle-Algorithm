class Solution(object):
    def countServers(self, grid):
        
        # 같은 열에 있거나 같은 행에 있는 서버의 개수
        # dfs connected component 시도해보기
        answer = set()
        n = len(grid)
        m = len(grid[0])


        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and (i, j):
                    is_comm = False
                    for k in range(i+1, n):
                        if grid[k][j] > 0:
                            is_comm = True
                            answer.add((k, j))
                    for k in range(j+1, m):
                        if grid[i][k] > 0:
                            is_comm = True
                            answer.add((i, k))
                    if is_comm:
                        answer.add((i, j))

        return len(answer)



sol = Solution()
# print(sol.countServers([[1,0],[0,1]]))
# print(sol.countServers([[1,0],[1,1]]))
print(sol.countServers([[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]))