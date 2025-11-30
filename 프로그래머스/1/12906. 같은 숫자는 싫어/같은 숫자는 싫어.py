def solution(arr):
    answer = []
    arr.reverse()
    while len(arr) > 0:
        l = len(answer)
        a = arr.pop()
        if l == 0:
            answer.append(a)
        elif answer[l-1] != a:
            answer.append(a)
           
    return answer