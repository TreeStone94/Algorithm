def solution(answers):
    answer = []
    
    
    # 수포자1: 1,2,3,4,5 (5개)
    # 수포자2: 2,1,2,3,2,4,2,5 (7개)
    # 수포자3: 3,3,1,1,2,2,4,4,5,5 (10개)
    reject_math_01 = [1,2,3,4,5]
    reject_math_02 = [2,1,2,3,2,4,2,5]
    reject_math_03 = [3,3,1,1,2,2,4,4,5,5]
    
    n_01 = len(reject_math_01)
    n_02 = len(reject_math_02)
    n_03 = len(reject_math_03)
    
    reject_math_cnt = [0]*3
    for i,a in enumerate(answers):
        if a == reject_math_01[(i)%n_01]:
            reject_math_cnt[0] += 1
        if a == reject_math_02[(i)%n_02]:
            reject_math_cnt[1] += 1
        if a == reject_math_03[(i)%n_03]:
            reject_math_cnt[2] += 1
            
    max_cnt = max(reject_math_cnt)
    for i,cnt in enumerate(reject_math_cnt):
        if max_cnt == cnt:
            answer.append(i+1)
        
    return answer