import collections

def solution(priorities, location):
    answer = 0
    
    """
        1. 우선순위가 높다는건 priorities의 값이 크다는 것이다
        2. 동일한 우선순위가 있으므로 내가 찾는 위치를 정확하게 알 수 있는 방법을 알아야 한다.
        
        1. 가장 큰값을 어떻게 구하실건가요?
        - max의 값 deque 지원
        2. 동일한 우선순위가 있을 때 어떻게 위치를 찾으실건가요?
    """
    tmp_list = []
    for i in range(len(priorities)):
        tmp_list.append((priorities[i],i))
    dp = collections.deque(tmp_list)
    
    result = []
    while dp:
        p = dp.popleft()
        if dp and p[0] < max(p for p,i in dp):
            dp.append(p)
        else:
            result.append(p)
    
    for i in range(len(result)):
        if result[i][1] == location:
                   answer = (i+1)
    return answer