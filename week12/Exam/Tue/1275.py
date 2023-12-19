class Solution(object):
    def tictactoe(self, moves):
        n = len(moves)

        board = [[0 for _ in range(3)]*3]
        
        # (0, 0) (0, 1) (0, 2)
        # (1, 0) (1, 1) (1, 2)
        # (2, 0) (2, 1) (2, 2)
        # (0, 0) (1, 0) (2, 0)
        # (0, 1) (1, 1) (2, 1)
        # (0, 2) (1, 2) (2, 2)
        # (0, 0) (1, 1) (2, 2) 6
        # (0, 2) (1, 1) (2, 0) 7
        cases = [0 for _ in range(8)]
        
        cnt = 0
        for i in range(n):
            x, y = moves[i]
            z = 1 if i % 2 == 0 else -1
            cases[x] += z
            cases[y+3] += z
            if x == y:
                if x == 1:
                    cases[7] += z
                cases[6] += z
            if abs(x-y) == 2:
                cases[7] += z
            cnt += 1
            for j in range(8):
                if cases[j] == 3:
                    return "A"
                if cases[j] == -3:
                    return "B"
        
        if cnt < 9:
            return "Pending"
        return "Draw"
            
            


sol = Solution()
# print(sol.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(sol.tictactoe([[0,0],[1,1]]))