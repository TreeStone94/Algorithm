n, m = map(int, input().split())

aArr = [0 for _ in range(n)]

for _ in range(m):
    i,j,k = map(int, input().split())
    for z in range(i-1,j):
        aArr[z] = k



for x in aArr:
    print(x, end = " ")