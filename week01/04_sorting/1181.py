
import sys


def compare(s1, s2):
    if len(s1) != len(s2):
        return len(s1) > len(s2)
    # ! 문자 하나씩 검색 -- 시간초과
    # for i in range(len(s1)):
    #     if s1[i] == s2[i]:
    #         continue
    #     return s1[i] < s2[i]
    # return False
    return s1 > s2


# def heapify(r, n, arr):
#     root = arr[r]
#     k = r*2+1
#     while k < n:
#         k = k+1 if k+1 < n and compare(arr[k+1], arr[k]) else k
#         if compare(root, arr[k]):
#             return
#         arr[(k-1)//2] = arr[k]
#         k = k*2+1
#     arr[k//2] = root


# def heap_sort(arr):
#     # 배열의 처음 상태를 힙으로 만들기
#     for i in range(len(arr)//2, -1, -1):
#         heapify(i, len(arr), arr)
#     # 루트 노드를 꺼내 엔드 노드와 교환합니다.
#     for i in range(len(arr)):
#         arr[len(arr)-1-i], arr[0] = arr[0], arr[len(arr)-1-i]
#         heapify(0, len(arr)-i-1, arr)
#     return


N = int(input())
words = [sys.stdin.readline().strip() for _ in range(N)]
words.sort()
words.sort(key=len)
words = set(words)
words = list(words)

for i in range(len(words)):
    print(words[i])


# heap_sort(words)
# for i in range(len(words)):
#     # 이미 정렬된 상태이므로
#     if i > 0 and words[i] == words[i-1]:
#         continue
#     print(words[i])
