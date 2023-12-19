

def mtxmulti(A, B):
    M = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(0, N):
                M[i][j] += A[i][k] * B[k][j]
            M[i][j] %= 1000
    return M


def solve(b):
    global mtx
    if b == 1:
        return mtx
    tmp = solve(b//2)
    if b % 2 == 0:
        return mtxmulti(tmp, tmp)
    return mtxmulti(mtx, mtxmulti(tmp, tmp))


N, B = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]

rtn = solve(B)

for i in range(N):
    for j in range(N):
        # B = 1인경우 원래 배열을 리턴하므로 출력할 때 한번 더 모듈러하여 프린트
        print(rtn[i][j] % 1000, end=' ')
    print()


'''
오답노트
B = 1인 경우를 고려하지 못함

input1
2 1
1000 1000
1000 1000

output1
0 0
0 0
'''
