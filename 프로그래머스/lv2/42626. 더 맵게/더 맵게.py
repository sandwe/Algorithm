import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + (second * 2)
        
        heapq.heappush(scoville, mixed)
        
        answer += 1
        
    if min(scoville) < K:
        answer = -1
    
    return answer