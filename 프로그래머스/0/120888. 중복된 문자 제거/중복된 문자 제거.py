def solution(my_string):
    # 대소문자 구분, 공백도 문자
    # 중복제거 set? count 배열? 
        # set를 써서하는게 맞을까?
    # 이미 단어가 중복으로 있다는걸 파악이후 위치에 대한 정보? or stack pop
    # {p:1,e:1,o:}
    answer = ''
    count_string = {}
    for s in my_string:
        if s not in count_string:
            count_string[s] = 1
        else:
            count_string[s] += 1
        
        if count_string[s] == 1:
            answer += s
            
    
    return answer