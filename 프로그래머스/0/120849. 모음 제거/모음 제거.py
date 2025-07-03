def solution(my_string):
    answer = ''
    m = ['a', 'e', 'i', 'o','u']
    for ms in my_string:
        if m.count(ms) == 0:
            answer += ms
    return answer