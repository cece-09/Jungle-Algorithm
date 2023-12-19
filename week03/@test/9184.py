def insert_table(M, N):
    for a in range(M, N+1):
        for b in range(M, N+1):
            for c in range(M, N+1):
                if a <= 0 or b <= 0 or c <= 0:
                    DP[(a, b, c)] = 1

                elif a > 20 or b > 20 or c > 20:
                    DP[(a, b, c)] = DP[(20, 20, 20)]

                elif a < b and b < c:
                    DP[(a, b, c)] = DP[(a, b, c-1)] + \
                        DP[(a, b-1, c-1)]-DP[(a, b-1, c)]

                else:
                    DP[(a, b, c)] = DP[(a-1, b, c)] + DP[(a-1, b-1, c)] + \
                        DP[(a-1, b, c-1)]-DP[(a-1, b-1, c-1)]


ints = []
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        ints.append((a, b, c))

DP = {}
insert_table(-50, 20)  # 20까지 채우고
insert_table(-50, 50)  # 다시 for문

for a, b, c in ints:
    print(f"w({a}, {b}, {c}) = {DP[(a, b, c)]}")
