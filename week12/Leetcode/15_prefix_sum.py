# reference: prefix sum algorithm
# 배열을 순차 탐색하면서 구간의 합을 구한다

class Solution(object):
    # sum이 k와 같은 subarray의 수 구하기
    def subarraySum(self, nums, k):
        n = len(nums)
        answer = 0
        hashmap = {}
        
        csum = 0
        for i in range(n):
            csum += nums[i]
            if csum == k:
                answer += 1
                
            if csum - k in hashmap:
                answer += hashmap[csum - k]

            if csum in hashmap:
                hashmap[csum] += 1
            else:
                hashmap[csum] = 1

        print(f"{nums}: {answer}")
        return answer
        

sol = Solution()
# sol.subarraySum([1, -1, 0], 0)
sol.subarraySum([1, 2, 3], 3)
# sol.subarraySum([1, 2, 3], 3)
