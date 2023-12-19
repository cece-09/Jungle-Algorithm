n = 8

def solution():

    def rfunc(m):
        if m == 0:
            return []
        if m == 1:
            return ["()"]
        
        rtn = []
        pairs = []
        for i in range(1, m):
            pairs.append((i, m-i))
        
        for s in rfunc(m-1):
            rtn.append("(" + s + ")")

        for p in pairs:
            s1 = rfunc(p[0])
            s2 = rfunc(p[1])

            for s in s1:
                for t in s2:
                    rtn.append(s + t)
        return rtn
        
    arr = rfunc(n)
    return list(dict.fromkeys(arr))

print(solution())
