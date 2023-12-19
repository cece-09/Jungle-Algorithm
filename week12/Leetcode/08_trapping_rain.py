class Solution(object):
    def trap(self, height):
        n = len(height)
        answer = 0

        lmax, rmax = -1, -1
        le, ri = 0, n-1

        while le < ri:
            if height[le] < height[ri]:
                lmax = max(lmax, height[le])
                answer += (lmax - height[le])
                le += 1
            else:
                rmax = max(rmax, height[ri])
                answer += (rmax - height[ri])
                ri -= 1
        
        return answer


sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([4,2,0,3,2,5]))