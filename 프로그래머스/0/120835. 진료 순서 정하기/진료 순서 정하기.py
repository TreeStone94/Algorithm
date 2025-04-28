def solution(emergency):
    answer = []
    es = sorted(emergency,reverse=True)
    for e in emergency:
        answer.append(es.index(e)+1)
            
    return answer
