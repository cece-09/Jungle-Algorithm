x = 1534236469

def solution():
    if x == 0:
        return 0
    
    is_negative = x < 0
    digits = list(str(x))

    if is_negative:
        digits = digits[1:]

    while digits[-1] == '0':
        digits.pop()

    y = 0
    tmp = 1
    for d in digits:
        y += int(d) * tmp
        tmp *= 10
    
    y = y * (-1 if is_negative else 1)

    lim = (1 << 31)
    if y > lim-1 or y < -1*lim:
        return 0
    
    return y

print(solution())

