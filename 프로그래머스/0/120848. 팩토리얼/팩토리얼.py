def solution(n):
    answer = 0
    result = 1
    for i in range(1,3628800+1):
        result = result *i
        if n >= result:
            answer = i
        elif n < result:
            break;
            
    return answer