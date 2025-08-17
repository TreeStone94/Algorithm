def solution(cipher, code):
    # 시작점::증가수
    answer = cipher[code-1::code]
    return answer
