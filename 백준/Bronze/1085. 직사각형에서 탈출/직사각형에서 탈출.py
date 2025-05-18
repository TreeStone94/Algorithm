x,y,w,h = map(int, input().split())

arr = []

arr.append(w-x)
arr.append(h-y)
arr.append(x)
arr.append(y)

print(min(arr))