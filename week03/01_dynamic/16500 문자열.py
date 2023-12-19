'''
👀 POINT
valid한 경우에 탈출하는 것이 아니라
invalid한 경우 탈출하도록 코드를 짜야 수행시간이 감소
'''

S = input().strip()
N = int(input())
A = [input().strip() for _ in range(N)]
M = len(S)


def solve(idx):
    global result
    if idx == M:  # idx가 len과 같음
        result = 1
        return
    if DP[idx]:
        return

    DP[idx] = 1  # 이 인덱스까지 체크

    for i in range(N):  # idx부터의 문자열이 일치하는지 여부 검사
        if len(S[idx:]) >= len(A[i]):
            # 각 문자가 일치하는지 여부 비교
            is_valid = True
            for j in range(len(A[i])):
                if A[i][j] != S[idx+j]:
                    is_valid = False
                    break
            if is_valid:
                solve(idx+len(A[i]))
    return


DP = [0]*M
result = 0
solve(0)
print(result)
