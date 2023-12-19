class Solution(object):
    # 반복되는 문자가 없는 가장 긴 문자열
    def lengthOfLongestSubstring(self, s):
        n = len(s)

        i, answer = 0, 0
        while i < n:
            # i부터 시작하는 repeatless substring
            letters = set()
            for j in range(i, n):
                if s[j] not in letters:
                    letters.add(s[j])
                else:
                    break
            answer = max(answer, len(letters))
            i += 1

        print(f"{s}: {answer}")
        return answer


sol = Solution()
sol.lengthOfLongestSubstring("abcabcbb")
sol.lengthOfLongestSubstring("bbbbb")
sol.lengthOfLongestSubstring("pwwkew")
sol.lengthOfLongestSubstring(" ")
