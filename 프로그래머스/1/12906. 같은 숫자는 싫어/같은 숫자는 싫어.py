from collections import deque
def solution(arr):
    answer = []
    
    arr = deque(arr)
    
    while arr:
        a = arr.popleft()
        if arr and a != arr[0]:
            answer.append(a)
            
        if not arr:
            answer.append(a)
        
        
    return answer