N = int(input())
A = list(map(int, input().split()))
S = [-1 for _ in range(N)]


def get_diff(i):
    if i < 1:
        return 0
    return abs(A[S[i-1]] - A[S[i]])


def search(n, cnt):
    global max
    if n == N:
        # update ans or not
        # print(S, cnt)
        if cnt > max:
            max = cnt
        return
    for i in range(len(A)):
        if not i in S:
            S[n] = i
            search(n+1, cnt + get_diff(n))
            S[n] = -1


max = 0
search(0, max)
print(max)
