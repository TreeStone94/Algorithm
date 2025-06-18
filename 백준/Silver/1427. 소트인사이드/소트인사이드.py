arr = list(input())

n = len(arr)

for i in range(n-1):
    l = i
    for j in range(i,n):
        if int(arr[j]) > int(arr[l]):
            l = j
    arr[i], arr[l] = arr[l], arr[i]

for a in arr:
    print(a,end="")