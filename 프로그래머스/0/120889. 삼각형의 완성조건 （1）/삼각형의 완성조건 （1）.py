def solution(sides):
    # 삼각형 조건: 최대값이 다른 두변의 길이보다 작아야함
    # 최대값 max, 두변의 길이
    _max = max(sides)
    answer = 0
    
    if _max < sum(sides) - _max:
        answer = 1
    else:
        answer = 2
    return answer