W, H = map(int, input().split())
N = int(input())

X = [0, W]
Y = [0, H]

# get data
for _ in range(N):
    flag, no = map(int, input().split())
    if flag == 0:
        Y.append(no)
    else:
        X.append(no)

X.sort()
Y.sort()

max = 0

# TODO 가로 중 최대, 세로 중 최대를 따로 구해서 곱하기
for i in range(len(X)-1):
    width = X[i+1] - X[i]
    for j in range(len(Y)-1):
        height = Y[j+1]-Y[j]
        if width * height > max:
            max = width * height

print(max)
