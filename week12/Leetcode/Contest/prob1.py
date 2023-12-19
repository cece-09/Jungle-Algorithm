class Solution(object):
    def findKOr(self, nums, k):
        # 각 배열에서 최소 k개 원소에 공통적으로 1인 비트
        n, m = len(nums), 0
        hashmap = {} # 비트 위치 저장
        for i in range(n):
            cnt, idx = 0, 0
            hashmap[i] = []
            while nums[i]:
                if nums[i] & 1:
                    hashmap[i].append(idx)
                    m = max(m, idx)
                
                idx += 1
                cnt += nums[i] & 1
                nums[i] >>= 1

        bits = [0 for _ in range(m+1)]
        for i in hashmap:
            for j in hashmap[i]:
                bits[j] += 1

        answer = 0
        for i in range(m+1):
            if bits[i] >= k:
                answer = answer | (1 << i)                
        
        return answer

sol = Solution()
sol.findKOr([2,12,1,11,4,5], 6)
sol.findKOr([7,12,9,8,9,15], 4)
sol.findKOr([10,8,5,9,11,6,8], 1)
        