def solution(age):
    answer = ''
    strAge = str(age)
    a = 'abcdefghijklmnopqrstuvwxyz'
    for x in strAge:
        answer += a[int(x)]
    return answer