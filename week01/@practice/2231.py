# 완전탐색
N = input()
M = 0

n = len(N)


def solve(n, sum, k, arr):
    global M
    if n == 0:
        m = int("".join(list(map(str, arr))))
        if sum + m == int(N):
            M = min(M, m) if M != 0 else m
        # print(f"[{m}] {sum+m} M: {M}")
        return
    for i in range(k):
        solve(n-1, sum + i, 10, arr+[i])


solve(n, 0, int(N[0])+1, [])
print(M)
