strs = ["flower","flow","flight"]

def solution():
    answer = ""
    n = len(strs)
    lens = [0 for _ in range(n)]
    
    # get lengths
    for i in range(n):
        lens[i] = len(strs[i])
    
    # get longest common prefix
    for i in range(min(lens)):
        c = strs[0][i]
        is_common = True
        for s in strs:
            if s[i] != c:
                is_common = False
                break

        if is_common:
            answer += c
        else:
            break
    
    return answer

print(solution())
        