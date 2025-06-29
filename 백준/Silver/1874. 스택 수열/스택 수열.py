n = int(input())

arr = []

printArr =[]
next_push = 1
for _ in range(n):
    inputNum = int(input())

    if inputNum >= next_push:
        for i in range(next_push, inputNum+1):
            arr.append(i)
            printArr.append('+')
        next_push = inputNum +1


    L = len(arr) - 1

    if L >= 0:
        top = arr[L]

        if top == inputNum:
            arr.pop()
            printArr.append('-')
        else:
            printArr.append('NO')




if printArr.count('NO') > 0:
    print('NO')
else:
    for p in printArr:
        print(p)