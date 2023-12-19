from collections import defaultdict
class Solution(object):
    def minimumCardPickup(self, cards):
        # 중복하는 값을 뽑기 위한 최소의 카드수
        n = len(cards)
        
        answer = float('inf')
        dic = defaultdict(int)
        for i in range(n):
            if cards[i] not in dic:
                dic[cards[i]] = i
                continue
            old = dic[cards[i]]
            answer = min(answer, (i-old+1))
            dic[cards[i]] = i
        
        if answer == float('inf'):
            return -1
        return answer