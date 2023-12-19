import sys

N, M = map(int, input().split())
cards = list(map(int, input().split()))
selected = [-1, -1, -1]

max = 0


def select_card(n, cnt):
    global max
    if n == 3:
        if max < cnt <= M:
            max = cnt
        return
    for i in range(len(cards)):
        if not i in selected:
            selected[n] = i
            select_card(n+1, cnt + cards[i])
            selected[n] = -1


select_card(0, max)
print(max)
