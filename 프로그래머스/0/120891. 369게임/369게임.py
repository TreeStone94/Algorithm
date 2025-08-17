def solution(order):
    # 키값에 a in d 가 있을 때 횟수 증가
    d = {'3','6','9'}
    answer = 0
    for o in str(order):
        if o in d:
            answer += 1
    return answer