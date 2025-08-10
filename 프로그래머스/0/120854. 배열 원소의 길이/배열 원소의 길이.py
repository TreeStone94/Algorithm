def solution(strlist):
    answer = []
    # str -> len으로 구하여 answer에 append
    for s in strlist:
        answer.append(len(s))
    return answer