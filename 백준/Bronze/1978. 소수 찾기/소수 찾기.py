cnt = 0
n = int(input())
arr = list(map(int, input().split()))

for a in arr:
    aCnt = 0
    for i in range(a):
        if a % (i+1) == 0:
            aCnt +=1
    if aCnt == 2 :
        cnt +=1


print(cnt)
