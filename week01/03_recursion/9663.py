# n = 보드 가로세로, 퀸의 수
# i = 현재 놓은 퀸의 수
# a = 퀸 좌표의 열 인덱스
# b = 퀸 좌표의 오른쪽 대각선 열 인덱스
# c = 퀸 좌표의 왼쪽 대각선 열 인덱스
def queens(n, i, a, b, c):
    global cnt
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        cnt += 1
        return


N = int(input())
cnt = 0
queens(N, 0, [], [], [])
print(cnt)
