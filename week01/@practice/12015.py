# Longest Increasing Sequence

def binary_search():
    R = [arr[0]]
    for i in range(1, N):
        # i를 가장 마지막 수로 하여 만들 수 있는 부분 증가 수열의 길이
        if arr[i] > R[-1]:
            R.append(arr[i])
            continue
        if arr[i] <= R[0]:
            R[0] = arr[i]
            continue

        s, e = 0, len(R)-1
        while s+1 < e:
            m = (s+e)//2
            if R[m] < arr[i]:
                s = m
            else:
                e = m
        R[e] = arr[i]
    return len(R)


def dp():  # Dynamic Programming
    DP = [1] * N  # i까지의 최장증가부분수열을 저장
    for i in range(1, N):
        DP[i] = 1  # 자기 자신
        for j in range(0, i):
            if arr[i] > arr[j]:
                DP[i] = max(DP[i], DP[j]+1)
    return DP[-1]


N = int(input())
arr = list(map(int, input().split()))

result = binary_search()
# result = dp()
print(result)
