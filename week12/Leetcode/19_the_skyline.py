from heapq import heappop, heappush

class Solution:
    def getSkyline(self, buildings):
        # 배열을 순차적으로 훑으면서
        # 겹치는 좌표를 만나면 처리
        # answer에 추가할 점 좌표
        tuples = [(L, -H, R) for L, R, H in buildings]
        tuples +=  [(R, 0, -1) for _, R, _ in buildings]
        tuples.sort()
        
        # max heap에는 왼쪽 점의 (y, x)좌표를 저장
        # 힙이 empty되지 않도록 min, max로 초기화
        answer = [[0, 0]]
        max_heap = [(0, float('inf'))]
        for x, negative_height, R in tuples:
            while x >= max_heap[0][1]:
                # 만약 왼쪽 점의 x좌표값이 더 크면
                # 더 작은 점들을 반복적으로 제거
                # height 우선 정렬되어 있으므로 반복문 필요
                heappop(max_heap)
            if negative_height:
                # height값이 있으면 힙에 (height, R) 삽입
                # 오른쪽 점의 (y, x) 좌표
                heappush(max_heap, (negative_height, R))
            
            # 힙에서 최대 높이이 가져와서
            # answer 배열의 마지막 원소의 높이와 비교
            # 동일하지 않으면 answer 배열에 추가
            curr_max_height = -max_heap[0][0]
            if answer[-1][1] != curr_max_height:
                answer.append([x, curr_max_height])

        # 초기 (min, max)제외하고 answer 리턴
        return answer[1:] 



sol = Solution()
print(sol.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# print(sol.getSkyline([[0,2,3],[2,5,3]]))