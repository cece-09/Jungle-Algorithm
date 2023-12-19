# 못 풀었습니다.
P = input()
N = len(P)
'''
'''
stack = []
i = 0
for i in range(N):
    if P[i] == 'A':
        if len(stack) < 2:
            print('NP')
            exit()
        if len(stack) >= 2:
            prev = "".join([stack[-2], stack[-1]])
            # print(prev)
            if not prev == 'PP' and not prev == 'AP':
                print('NP')
                exit()
        continue
    stack.append(P[i])

if len(stack) % 2 == 0:
    print('NP')
    exit()
print('PPAP')
