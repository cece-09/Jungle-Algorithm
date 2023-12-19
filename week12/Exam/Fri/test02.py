from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        # k개를 제거하고 난 후
        # 가장 적은 유니크 수의 개수
        count = Counter(arr)

        # count가 적은 값을 먼저 제거
        # unique = list(count.keys())
        # unique.sort(key=lambda x: count[x])

        # 여기서 값을 기준으로 sorting하여
        # 개수만 출력해도 OK
        values = list(count.values())
        values.sort()

        i = 0
        while k > 0:
            if values[i] <= k:
                k -= values[i]
                i += 1
            else:
                break

        return len(values) - i