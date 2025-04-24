a,b = [], []
n, m = map(int, input().split())

for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

for i in range(n):
    x = list(map(int, input().split()))
    b.append(x)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()