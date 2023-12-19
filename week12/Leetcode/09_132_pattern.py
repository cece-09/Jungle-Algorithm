class Solution:
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]

        # i번째 원소보다 더 앞에 있는
        # 원소 중 최솟값의 배열
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False


sol = Solution()
# print(sol.find132pattern([1,2,3,4]))
# print(sol.find132pattern([3,1,4,2]))
# print(sol.find132pattern([-1,3,2,0]))
# print(sol.find132pattern([1,0,1,-4,-3]))
# print(sol.find132pattern([3,5,0,3,4]))
# print(sol.find132pattern([1,0,1,-4,-3]))
# print(sol.find132pattern([1,4,0,-1,-2,-3,-1,-2]))
print(sol.find132pattern([1,2,3,4,-4,-3,-5,-1]))