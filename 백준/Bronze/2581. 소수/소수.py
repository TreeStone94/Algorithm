m = int(input())
n = int(input())



arr = []

for i in range(m,n+1):
    error = 0
    if i > 1:
        for n in range(2, i):
            if i % n == 0:
                error +=1
                break

        if error == 0 :
            arr.append(i)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)