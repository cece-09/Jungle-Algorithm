N = int(input())

if N % 2 == 0:
    print('CY')
else:
    print('SK')


# import sys

# N = int(sys.stdin.readline())

# DP = [-1] * (N + 1)
# DP[0] = 0
# DP[1] = 1  # SK

# for i in range(2, N + 1):
#     if DP[i - 1] == 1 or DP[i - 3] == 1:
#         DP[i] = 0
#     else:
#         DP[i] = 1

# if DP[N] == 1:
#     print("SK")
# else:
#     print("CY")
