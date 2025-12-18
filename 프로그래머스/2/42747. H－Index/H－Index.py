def solution(citations):
    # 내림차순 정렬: [6, 5, 3, 1, 0]
    citations.sort(reverse=True)
    
    h = 0
    for i, citation in enumerate(citations):
        # i+1 = 현재까지 본 논문 수 (h 후보)
        # citation = 현재 논문의 인용 횟수
        
        if citation >= i + 1:
            h = i + 1
        else:
            break
    
    return h