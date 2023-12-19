from collections import Counter
class Solution(object):
    def minSum(self, nums1, nums2):
        def check(esum, s1, s2, z1, z2):
            if esum-s1 >= z1 and esum-s2 >= z2:
                return True
            return False
        
        # 0을 양의 정수로 교체한 후
        # 얻을 수 있는 가장 작은 공통의 합
        s1, s2 = sum(nums1), sum(nums2)
        c1, c2 = Counter(nums1), Counter(nums2)
        z1, z2 = c1[0], c2[0]

        if z1 == 0 and s2+z2 > s1:
            return -1
        if z2 == 0 and s1+z1 > s2:
            return -1

        lo, hi = max(z1, z2), s1+s2+z1+z2 # !
        if check(lo, s1, s2, z1, z2):
            return lo
        
        if not check(hi, s1, s2, z1, z2):
            return -1
        
        while lo+1 < hi:
            mid = (lo+hi)//2
            if check(mid, s1, s2, z1, z2):
                hi = mid
            else:
                lo = mid
        
        return hi




sol = Solution()
print(sol.minSum([0,0], [26,5,7,0,1,3,0,7,0,0,5,25,26,20,0,3,20,23,18]))
# sol.minSum([3,2,0,1,0], [6,5,0])