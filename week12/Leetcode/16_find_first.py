
class Solution(object):
    def searchRange(self, nums, target):
        # non-decreasing order로 정렬되어 있는 array에서
        # target value의 시작과 끝 구간 찾기
        def binary_search(flag, nums, tar, lo, hi):
            while lo+1 < hi:
                mid = (lo+hi)//2
                if flag == 0:  # lower bound
                    if nums[mid] < tar:
                        lo = mid
                    else:
                        hi = mid
                else:         # upper bound
                    if nums[mid] <= tar:
                        lo = mid
                    else:
                        hi = mid
            
            rtn = lo if flag else hi
            return rtn if nums[rtn] == tar else -1


            
        answer = [-1, -1]
        n = len(nums)
        lo, hi = 0, n-1

        # exceptions
        if n == 0:
            return answer
        if n == 1:
            e = 0 if nums[0] == target else -1
            return [e, e]
        if nums[lo] > target or nums[hi] < target:
            return answer
        
        answer[0] = binary_search(0, nums, target, lo, hi)
        answer[1] = binary_search(1, nums, target, lo, hi)

        if nums[lo] == target:
            answer[0] = lo

        if nums[hi] == target:
            answer[1] = hi

        return answer