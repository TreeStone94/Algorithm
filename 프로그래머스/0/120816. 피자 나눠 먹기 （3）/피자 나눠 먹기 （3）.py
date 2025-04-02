def solution(slice, n):
    answer = 0
    if slice > n:
        answer = 1
    else:
        i = 0
        if n % slice > 0:
            i += 1
        answer = (n // slice) + i
    
    return answer