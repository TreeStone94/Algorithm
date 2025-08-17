def solution(cipher, code):
    # 배수를 구하는 프로세스가 필요 배열에 넣고 answer에 더하기
    # 문자열 길이보다 크면 배수 정지, 문자열을 저장하는 변수 필요
    cipher_len = len(cipher)
    codeArr = []
    
    code_b = 1
    for i in range(1,1001):
        code_b = code * i
        if code_b > cipher_len:
            break
        else:
            codeArr.append(code_b)
    
    answer = ''
    for c in codeArr:
        answer += cipher[c-1] 
    return answer