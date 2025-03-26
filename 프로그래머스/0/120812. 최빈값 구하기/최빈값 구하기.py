def solution(array):
    xarray = list(set(array))
    
    answer = 0
    cnt = []
    for x in xarray:
        cnt.append(array.count(x))
        
    if cnt.count(max(cnt)) > 1:
        answer = -1
    else:
        answer = xarray[cnt.index(max(cnt))]
    return answer