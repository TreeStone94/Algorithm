def solution(array, n):
    # 차이를 저장하는 딕셔너리, 배열의 가장 작은수 min
    # 20 - 28 = 8
    # 20 - 12 = 8
    # 그러면 12를 선택해야함
    
    darray = []
    for a in sorted(array):
        if n >= a:
            darray.append(n-a)
        else:
            darray.append(a-n)
    
    answer = sorted(array)[darray.index(min(darray))]
    return answer