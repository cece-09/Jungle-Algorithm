from collections import Counter
class Solution(object):
    def removeDigit(self, number, digit):
        n = len(number)
        answer = 0
        
        c = Counter(number)
        print(c)
        for i in range(n):
            if number[i] == digit:
                if i+1 < n and int(number[i+1]) > int(digit):
                    return number[:i]+number[i+1:]
                if c[number[i]] == 1:
                    return number[:i]+number[i+1:]
                else:
                    c[number[i]] -= 1
        
        return str(answer)

sol = Solution()
# print(sol.removeDigit("1231", "1"))
print(sol.removeDigit("123", "3"))