
class Solution(object):
    def findKthLargest(self, nums, k):

        def rfunc(arr, n, k):
            if n == 1:
                return arr[0]
            
            pivot = arr[0]
            sm, lg, eq = [], [], []
            scnt, ecnt, lcnt = 0, 0, 0
            for num in arr:
                if num < pivot:
                    sm.append(num)
                    scnt += 1
                elif num == pivot:
                    eq.append(num)
                    ecnt += 1
                else:
                    lg.append(num)
                    lcnt += 1
            
            if k <= lcnt:
                # k is in large group
                return rfunc(lg, lcnt, k)
            
            if k <= lcnt + ecnt:
                # k is in equal group
                if ecnt == n:
                    # if all elements are the same
                    # return the first
                    return eq[0]
                return rfunc(eq, ecnt, k - lcnt)

            if k <= lcnt + ecnt + scnt:
                # k is in small group
                return rfunc(sm, scnt, k - lcnt - ecnt)
        
        # call recursive
        # quickselect function
        n = len(nums)
        return rfunc(nums, n, k)

        
        
sol = Solution()
sol.findKthLargest([5,2,4,1,3,6,0], 4)