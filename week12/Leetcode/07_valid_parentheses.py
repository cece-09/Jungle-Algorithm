s = "["


def solution():
    stack = []
    valid = True
    pair = {}

    pair[')'] = '('
    pair['}'] = '{'
    pair[']'] = '['

    for c in s:
        # if c is open bracket,
        if c in pair.values():
            stack.append(c)
            continue
        
        # if c is close bracket
        chk = pair[c]
        if len(stack) == 0:
            valid = False
            break

        if stack[-1] != chk:
            valid = False
            break
        stack.pop()

    if len(stack) > 0:
        valid = False

    return valid


print(solution())
