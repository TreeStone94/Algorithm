def solution(progresses, speeds):
    answer = []

    """
        progresses별 작업 일자 구하는 방법
            1. 100 - 30 = 70
            2. 70//30 = 2
            3. 70%30 != 0 -> 1

        배포 카운트 구하는 방법
            작업 일자 [1, 20, 1, 1, 10, 5]
            작업 일자가 없을때 까지
            day = 작업일자.pop()
            if day >= 작업일자[nextIndex]
                    작업일자.pop()

    """
    days = []
    while progresses:
        progress = progresses.pop()
        speed = speeds.pop()
        remain_progress = 100 - progress
        day = remain_progress // speed
        if remain_progress % speed != 0:
            day += 1
        days.append(day)

    count = 0

    while days:
        day = days.pop()
        count += 1
        while days and day >= days[-1]:
            days.pop()
            count += 1
        answer.append(count)
        count = 0

    return answer