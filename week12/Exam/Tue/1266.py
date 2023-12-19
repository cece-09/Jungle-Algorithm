
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        # points배열에 따라 주어진 순서로
        # 모든 점을 방문하는 최소 시간 구하기
        n = len(points)
        
        # O(n) time complexity
        answer = 0
        for i in range(n-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]

            dx = abs(x1-x2)
            dy = abs(y1-y2)
            answer += (dx+dy) - min(dx, dy)
        
        return answer



        
sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))