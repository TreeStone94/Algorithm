n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))


arr = sorted(arr, key= lambda p : (p[1],p[0]))

for a in arr:
    print(a[0],a[1])