n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))


arr = sorted(arr)

for a in arr:
    print(a[0],a[1])