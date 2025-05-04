def solution(balls, share):
    n=1
    nr = 1
    r=1
    for i in range(balls+1,1,-1):
       n = n*(i-1)
    
    for i in range(balls-share+1,1,-1):
        nr = nr*(i-1)
    
    for i in range(share+1,1,-1):
        r = r*(i-1)
        
    answer = n//(nr*r )
    return answer