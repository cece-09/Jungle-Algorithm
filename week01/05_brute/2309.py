import sys
height = [int(sys.stdin.readline()) for _ in range(9)]

height.sort()
sumh = sum(height)
for i in range(len(height)):
    is_found = False
    for j in range(i, len(height)):
        if sumh - (height[i] + height[j]) == 100:
            is_found = True
            break
    if is_found:
        break

for k in range(len(height)):
    if i == k or j == k:
        continue
    print(height[k])
