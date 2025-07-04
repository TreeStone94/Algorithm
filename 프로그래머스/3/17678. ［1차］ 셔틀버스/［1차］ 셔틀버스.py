def changeTime(time):
    sTime = time.split(':')
    return int(sTime[0])*60 + int(sTime[1])

def changeTimeStr(time):
    h = time//60
    m = time%60
    
    hh = str(h)
    if h < 10:
        hh = '0'+hh
    
    mm = str(m)
    if m < 10:
        mm = '0' + mm
    return hh + ':' + mm


def solution(n, t, m, timetable):
    answer = ''

    timeM = []
    for time in timetable:
        timeM.append(changeTime(time))

    timeQueue = []
    startAt = changeTime('09:00')
    print(startAt)
    for _ in range(n):
        timeQueue = []
        count = 0
        for tm in sorted(timeM):
            if startAt >= tm and count < m:
                timeQueue.append(tm)
                count +=1

        for q in timeQueue:
            timeM.remove(q)
        startAt += int(t)

    if len(timeQueue) < m:
        answer = changeTimeStr(startAt - t)
    else:
        answer = changeTimeStr(timeQueue[-1] - 1)
    return answer


