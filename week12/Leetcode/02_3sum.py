from itertools import combinations

nums = [-1, 0, 1, 2, -1, -4]

# 합이 0이 되는 케이스를 모두 출력


def solve():
    solution = set()
    answer = []
    N = len(nums)

    nums.sort()

    for i in range(N):
        j = N-1

        while i+1 < j:
            min_num = nums[i+1]
            max_num = nums[j-1]

            two_sum = nums[i] + nums[j]
            target = two_sum * (-1)

            # 이미 찾은 경우
            if target == min_num:
                solution.add((nums[i], min_num, nums[j]))
                j -= 1
                continue

            if target == max_num:
                solution.add((nums[i], max_num, nums[j]))
                j -= 1
                continue

            # 탐색이 필요없는 경우
            if target < min_num or target > max_num:
                j -= 1
                continue

            # target을 찾아본다
            low, high = i+1, j-1
            while low+1 < high:
                mid = (low+high)//2
                if nums[mid] < target:
                    low = mid
                else:
                    high = mid
            
            if nums[high] == target:
                solution.add((nums[i], nums[high], nums[j]))
            
            j -= 1

    answer = list(map(list, solution))
    return answer

print(solve())
