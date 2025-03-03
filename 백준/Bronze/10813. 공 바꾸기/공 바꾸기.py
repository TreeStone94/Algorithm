n, m = map(int, input().split())
aArr = [i+1 for i in range(n)]

for _ in range(m):
    i,j = map(int, input().split())
    tmpNum = aArr[i-1]
    aArr[i-1] = aArr[j-1]
    aArr[j-1] = tmpNum



for x in aArr:
    print(x, end = " ")