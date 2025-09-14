
import math

def solution(progresses, speeds):
    answer = []
    
    
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    count = 1
    currentDay = days[0]
    for d in days[1:]:
        if d <= currentDay:
            count += 1
        else:
            answer.append(count)
            count = 1
            currentDay = d
    answer.append(count)
    
   
    # 작업속도와 진행률
    # 첫번째 작업이 7일, 두번째 3일, 세번째 9일
    # 7일 pop, 이전 index와 비교 이전 인덱스보다 작으면 count
    
    # 문제의 의도: 선입선출로 먼저들어온 진행률이 끝날때 까지 기다렸다가 같이 배포해야한다.
    
                
        
    return answer