nums = [4, 4, 2, 4, 3]

# unequal 부분수열
def solution():
    N = len(nums)
    answer = 0

    for i in range(N):
        j = i+1

        while j < N-1:
            if nums[i] == nums[j]:
                j += 1
                continue

            k = N-1
            # nums[i] != nums[j]인 위치
            while j < k:
                if nums[j] == nums[k]:
                    k -= 1
                    continue
                elif nums[i] == nums[k]:
                    k -= 1
                    continue
                else:
                    answer += 1
                    k -= 1
            j += 1
   
    return answer

print(solution())