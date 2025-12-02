from collections import deque

def solution(progresses, speeds):
    answer = []

    days = deque()
    for progress, speed in zip(progresses, speeds):
        day = -(-(100 - progress) // speed)
        days.append(day)

    while days:
        current_day = days.popleft()
        count = 1
        while days  and current_day >= days[0]:
            days.popleft()
            count +=1
        answer.append(count)

    return answer