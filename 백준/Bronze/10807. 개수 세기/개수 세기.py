cnt = int(input())
xArr = list(map(int, input().split()))
findNum = int(input())
findCnt = 0

for x in xArr:
    if x == findNum:
        findCnt += 1

print(findCnt)