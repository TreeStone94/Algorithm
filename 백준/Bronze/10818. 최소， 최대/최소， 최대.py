n = int(input())
aArr = list(map(int, input().split()))

aArr.sort()
len = len(aArr)
print(aArr[0],aArr[len-1])