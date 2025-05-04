n = int(input())
cnt = 1
rangeNum = 1

while n > rangeNum:
    rangeNum += 6*cnt
    cnt +=1

print(cnt)