def solution(n):
    answer = []
    # 1 ~ 24까지 몫이 0인 수들을 배열에 추가
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)
    return answer