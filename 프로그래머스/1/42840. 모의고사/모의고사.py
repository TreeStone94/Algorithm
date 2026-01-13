def solution(answers):
    answer = []
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    # 점수 저장하는 배열 0,1,2,3,4,5
    scores = []
    
    for pattern in patterns:
        score = sum(1 for i,a in enumerate(answers) if a == pattern[i%len(pattern)])
        scores.append(score)
        
    max_score = max(scores)
    for i,s in enumerate(scores):
        if s == max_score:
            answer.append(i+1)
    return answer