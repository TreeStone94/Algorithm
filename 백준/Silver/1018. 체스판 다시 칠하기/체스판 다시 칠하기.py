arr = []
n, m = map(int,input().split())
for _ in range(n):
    arr.append(list(input()))


cnt = []
for i in range(n-7):
    for j in range(m-7):

        bcnt = 0
        wcnt = 0
        for a in range(i,8+i):
            for b in range(j,8+j):
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'W':
                        wcnt +=1
                    else:
                        bcnt +=1
                else:
                    if arr[a][b] != 'B':
                        wcnt += 1
                    else:
                        bcnt += 1
        cnt.append(wcnt)
        cnt.append(bcnt)


print(min(cnt))