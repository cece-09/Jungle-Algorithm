
class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = [set(), set()]
        for num in nums1:
            if num not in nums2:
                answer[0].add(num)
        
        for num in nums2:
            if num not in nums1:
                answer[1].add(num)
                
        answer = list(map(list, answer))
        return answer

        