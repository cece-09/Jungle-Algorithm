N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    is_prime = True
    if num == 2 or num == 1:
        cnt += num == 2
        continue
    for i in range(2, num//2 + 1):
        if num % i == 0:
            is_prime = False
            break
    cnt += is_prime
print(cnt)
