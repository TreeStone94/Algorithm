def solution(my_string):
    answer = 0
    
    for m in my_string:
        if m.isdecimal():
            answer += int(m)
            
    return answer