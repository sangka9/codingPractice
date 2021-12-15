#테스트 연습 - 힙(Heap) - 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for i in scoville :
        heapq.heappush(heap, i)
    # heapq.heapify(heap) 같은 코드

    while (1) :
        if len(heap) == 1 and heap[0] < K :
            answer = -1
            break
        
        if heap[0] >= K :
            break
        
        tmp1 = heapq.heappop(heap)
        tmp2 = heapq.heappop(heap)
        heapq.heappush(heap, tmp1 + (tmp2 * 2))
        
        answer += 1

    return answer
