N = int(input())


def is_han(N):
    digit = list(map(int, str(N)))
    if len(digit) == 1:
        return True
    gap = digit[1] - digit[0]
    for i in range(1, len(digit)):
        if digit[i] - digit[i-1] != gap:
            return False
    return True


cnt = 0
for i in range(1, N+1):
    cnt += is_han(i)
print(cnt)
