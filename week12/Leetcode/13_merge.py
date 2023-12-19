from heapq import heappop, heappush

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

def solution():
    # start를 기준으로 정렬
    intervals.sort(key=lambda x: x[0])

    answer = []
    
    # start가 빠른순으로 체크
    for interval in intervals:
        # start가 가장 늦은 interval의 end가 interval의 시작보다 빠른 경우
        if not answer or answer[-1][1] < interval[0]:
            answer.append(interval)
        else:
            # 오버랩 발생 (같거나 늦음)
            answer[-1][1] = max(answer[-1][1], interval[1])


    return answer
        
print(solution())


