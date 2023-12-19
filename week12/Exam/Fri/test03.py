
class Solution(object):
    def minDays(self, bloomDay, m, k):
        def available(days, m, k, n):
            # make m bouquets
            p, bouq = 0, 0
            while p < n:
                if bloomDay[p] > days:
                    bouq = 0
                    p += 1
                    continue

                bouq += 1
                if bouq == k:
                    m -= 1
                    bouq = 0
                
                if m <= 0:
                    return True
                
                p += 1

            return m <= 0
        

        n = len(bloomDay)

        # if it's impossible to make
        # m bouquets, return -1
        if n < m*k:
            return -1
        
        # find mininum num of days
        # by binary search
        lo, hi = min(bloomDay), max(bloomDay)

        # exceptions
        if available(lo, m, k, n):
            return lo
        
        if not available(hi, m, k, n):
            return -1
        
        while lo+1 < hi:
            mid = (lo+hi) // 2
            if available(mid, m, k, n):
                hi = mid
            else:
                lo = mid
        
        return hi


sol = Solution()
# sol.minDays([1,10,3,10,2], 3, 1)
# sol.minDays([1,10,3,10,2], 3, 2)
# sol.minDays([7,7,7,7,12,7,7], 2, 3)
sol.minDays([5,37,55,92,22,52,31,62,99,64,92,53,34,84,93,50,28], 8, 2)