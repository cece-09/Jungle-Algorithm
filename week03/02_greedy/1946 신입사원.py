import sys

T = int(input())


for _ in range(T):
    N = int(input())
    applicants = [tuple(map(int, sys.stdin.readline().split()))
                  for _ in range(N)]

    # 서류점수순으로 정렬
    applicants.sort()

    # 면접순으로 정렬했을때의 인덱스 구하기
    interview = sorted(applicants, key=lambda x: x[1])

    tmp = N
    cnt = 0
    for i in range(N):  # binary search
        tar = applicants[i][1]

        s, e = 0, N-1
        if interview[0][1] == tar:  # all T
            e = 0
        else:
            while s+1 < e:
                m = (s+e)//2
                if interview[m][1] >= tar:
                    e = m
                else:
                    s = m

        if tmp > e:
            cnt += 1
            tmp = e
    print(cnt)
