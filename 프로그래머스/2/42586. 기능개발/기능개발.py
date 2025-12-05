def solution(progresses, speeds):
    """
        1. 날짜구하기
        100 - 93 = 
        7//speed  = 7
        2. pop, append
        [7,3,9]
    """
    days = []
    while progresses:
        progress = progresses.pop()
        speed = speeds.pop()
        day = -(-(100 - progress) // speed)
        days.append(day)
    
    answer = []
    while days:
        count = 1
        day = days.pop()
        while days and day >= days[-1]:
            days.pop()
            count +=1
        answer.append(count)
    
    return answer