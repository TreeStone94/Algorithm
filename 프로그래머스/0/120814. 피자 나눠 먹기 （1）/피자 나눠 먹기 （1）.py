def solution(n):
    answer = 0
    if n <= 7:
        answer = 1
    else:
        a = 0
        if int(n%7) > 0:
            a = 1
        answer = n//7 + a
    return answer