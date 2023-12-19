x = 123


def is_palindrome():
    if x < 0:
        return False
    
    if x == 0:
        return True

    digits = list(str(x))
    while digits[-1] == '0':
        digits.pop()
    
    y = 0
    tmp = 1
    for i in range(len(digits)):
        y += int(digits[i])*tmp
        tmp *= 10

    return x == y

print(is_palindrome())