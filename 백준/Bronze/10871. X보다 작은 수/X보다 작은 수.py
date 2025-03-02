n, x = map(int, input().split())
aArr = list(map(int, input().split()))

for a in aArr:
    if a < x:
        print(a, end=" ")