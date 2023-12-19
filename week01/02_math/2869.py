A, B, V = map(int, input().split())

O = A - B
if V == A:
    print(1)
else:
    print((V-A-1) // O + 2)
