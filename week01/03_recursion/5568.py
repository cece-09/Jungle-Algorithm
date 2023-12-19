# Recursive
# https://www.acmicpc.net/problem/5568

N = int(input())
K = int(input())
C = [input() for _ in range(N)]

S = [[0 for _ in range(N)] for _ in range(K)]
integers = []

'''

get_integer(n):
  IF n == 마지막 카드라면:
    선택된 카드로 정수 만들기
    if not 이미 만든 정수:
      print(정수)
    return
  ELSE
    for card in all cards:
      if card is selected:
        continue
      select card
      get_integer(n+1) // 재귀: 다음 카드 선택
      unselect card

'''


def get_integer(no):
    if no == K:
        integer = ''.join([selected(i) for i in range(K)])
        if not integer in integers:
            integers.append(integer)
        return
    for i in range(len(C)):
        if is_selected(i):
            continue
        S[no][i] = 1
        get_integer(no+1)
        S[no][i] = 0


def is_selected(idx):
    for i in range(K):
        if S[i][idx] == 1:
            return True
    return False


def selected(no):
    for i in range(len(S[no])):
        if S[no][i] == 1:
            return C[i]


get_integer(0)
print(len(integers))
