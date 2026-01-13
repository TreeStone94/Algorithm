import heapq

def solution(k, score):
    result = []
    
    # 최소힙
    heap = []
    heapq.heapify(heap)    

    """
        10 -> heap = [10]
        100 -> heap = [10,100]
        20 -> heap = [10,20,100]
        150 -> heap = [10,20,100,150]
            -> heap[0] = 10
            -> 150
            -> [20,100,150]
        1   -> [1,20,100,150]
        
    """    
    for s in score:
        
        # heap 배열 길이가 k보다 작을때 heap
        if len(heap) < k: 
            heapq.heappush(heap, s)
        else:
            if heap[0] < s:
                # heapq.heappop()
                # heapq.heappush(heap,s)
                heapq.heapreplace(heap, s)
                
        result.append(heap[0])
        
            
    return result