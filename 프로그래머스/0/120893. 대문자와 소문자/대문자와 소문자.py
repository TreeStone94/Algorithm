def solution(my_string):
    # 대문자, 소문자를 구분할수 있는 아스키코드
    # ord 함수: 97->a, A->65, chr함수: 97->a, 65->A
    # 97보다 작으면 대문자, 크면 소문자
    # 12차이남, 소문자에서 대문자 97-32, 대문자에서 소문자 65+32
    
    answer = ''
    
    for m in my_string:
        o = ord(m)
        if o < 97:
            answer += chr(o+32)
        else:
            answer += chr(o-32)
            
        
    
    return answer