n, m = map(int, input().split())
aArr = [i+1 for i in range(n)]

for _ in range(m):
    i,j = map(int,input().split())
    bArr = list(reversed(aArr[i-1:j]))
    if i != j:
        a = 0
        for z in range(i-1, j):
           aArr[z] = bArr[a]
           a +=1

for x in aArr:
    print(x, end= " ")