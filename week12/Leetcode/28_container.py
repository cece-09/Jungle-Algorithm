class Solution(object):
    def maxArea(self, height):
        n = len(height)

        s, e = 0, n-1
        answer = (e-s)*min(height[s], height[e])
        while s < e:
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
            area = (e-s)*min(height[s], height[e])
            answer = max(answer, area)

        return answer
            


sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,2,4,3]))
print(sol.maxArea([3,2,1,3]))
print(sol.maxArea([2,3,10,5,7,8,9]))