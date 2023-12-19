# 2진법에서 1의 개수 세기
import random
import time


random_numbers = []
for _ in range(10000):
    num = random.randint(2**62, 2**63 - 1)
    random_numbers.append(num)


def func1(N):
    binary = bin(N)[2:]  # 2진수로 변환 후 'Ob' 제거
    cnt = binary.count('1')
    return cnt


def func2(N):
    cnt = 0
    while N:
        N = N & (N-1)
        cnt += 1
    return cnt


def func3(N):
    cnt = 0
    while N:
        cnt += N % 2
        N //= 2

    return cnt


def func4(N):
    cnt = 0
    i = 1

    while N:
        cnt += N & 1  # 현재 가장 오른쪽 비트가 1인지 확인
        N >>= 1       # N을 오른쪽으로 1 비트씩 이동하여 다음 비트 확인

    return cnt


start = time.time()
for each in random_numbers:
    cnt = func1(each)
end = time.time()
print(f"func 1: {cnt}, {end-start:.5f} sec")


start = time.time()
for each in random_numbers:
    cnt = func2(each)
end = time.time()
print(f"func 2: {cnt}, {end-start:.5f} sec")


start = time.time()
for each in random_numbers:
    cnt = func3(each)
end = time.time()
print(f"func 3: {cnt}, {end-start:.5f} sec")

start = time.time()
for each in random_numbers:
    cnt = func4(each)
end = time.time()
print(f"func 4: {cnt}, {end-start:.5f} sec")
