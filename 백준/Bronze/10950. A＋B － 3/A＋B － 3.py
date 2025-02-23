x = int(input())

xArr = []
for _ in range(x):
    a,b = map(int, input().split())
    xArr.append(a)
    xArr.append(b)

j = 0
for i in range(x):
    print(xArr[j+i] + xArr[j+i+1])
    j += 1

