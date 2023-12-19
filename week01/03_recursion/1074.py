# x, y 왼쪽 위 모서리 좌표
# num 한 변의 길이
# cnt (x, y) 까지 오기 위한 횟수

def visit(x, y, num, cnt):
    if num == 1:
        print(cnt)
        return

    num //= 2  # 한 변의 길이를 1/2
    ranges = [(x, y), (x, num+y), (num+x, y), (num+x, num+y)]

    for i, rng in enumerate(ranges):
        add_cnt = ((num*2)**2//4) * i
        if r in range(rng[0], rng[0]+num) and c in range(rng[1], rng[1]+num):
            visit(rng[0], rng[1], num, cnt+add_cnt)
        else:
            continue


N, r, c = map(int, input().split())
r += 1
c += 1
arr = 2 ** N
visit(1, 1, arr, 0)
