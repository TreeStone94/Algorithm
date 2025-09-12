import collections

def solution(arr):
    answer = []
    
    dq = collections.deque(arr)

    preNum = - 1
    while dq:
        num = dq.popleft()
        if preNum != num :
            answer.append(num)
        preNum = num
    return answer