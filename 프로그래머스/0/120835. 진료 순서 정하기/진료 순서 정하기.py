def solution(emergency):
    answer = []
    es = sorted(emergency,reverse=True)
    for e in emergency:
        for i in range(len(emergency)):
            if es[i] == e:
                answer.append(i+1)
            
    return answer