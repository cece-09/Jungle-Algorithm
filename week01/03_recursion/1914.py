N = int(input())


def hanoi(disk, start, inter, destn):
    global cnt
    if disk == 1:
        print(start, destn)
        return
    else:
        hanoi(disk-1, start, destn, inter)
        print(start, destn)
        hanoi(disk-1, inter, start, destn)


print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)
