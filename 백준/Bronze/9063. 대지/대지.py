n = int(input())

xArr = []
yArr = []

for _ in range(n):
    x,y = map(int,input().split())
    xArr.append(x)
    yArr.append(y)

print((max(xArr) - min(xArr))*(max(yArr) - min(yArr)))