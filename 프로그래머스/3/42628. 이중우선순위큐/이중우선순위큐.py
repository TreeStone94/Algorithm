import heapq

def solution(operations):
    answer = []
    # split하여 명령어 숫자를 구분
    # heapq 사용 최대값  -pop, 최솟값 pop
    heap = []
    
    for operation in operations:
        cmd, number = operation.split()
        if cmd == 'I':
            heapq.heappush(heap, int(number))
        elif cmd == 'D' and heap:
            if number == '1':
                heap.remove(max(heap))
                heapq.heapify(heap)
            elif number == '-1':
                heapq.heappop(heap)
  
    if heap:
        answer = [max(heap), min(heap)]
    else:
        answer = [0,0]
    
    return answer