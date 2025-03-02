n, x = map(int, input().split())
aArr = list(map(int, input().split()))

printStr = ''
for a in aArr:
    if a < x:
        printStr += str(a) + " "

print(printStr)