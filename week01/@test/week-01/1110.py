def solve(n):
    global cnt
    if n == N and cnt > 0:
        return

    if n < 10:
        v1, v2 = 0, n
    else:
        v1, v2 = n//10, n-(n//10*10)
    v3 = v1+v2 if v1+v2 < 10 else (v1+v2)-((v1+v2)//10 * 10)
    cnt += 1
    solve(v2*10+v3)


N = int(input())
cnt = 0
solve(N)
print(cnt)
