def changeToint(a,b):
    return int(str(a) + str(b))
    
def solution(a, b):
    answer = 0
    
    ab = changeToint(a,b)
    ba = changeToint(b,a)
    
    if ab > ba:
        answer = ab
    else:
        answer = ba
    
   
    return answer