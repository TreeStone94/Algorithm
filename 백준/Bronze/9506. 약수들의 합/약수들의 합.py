while True:
    n = int(input())

    if n == -1:
        break

    arr = []
    for i in range(n):
        if (i+1) != n and n % (i+1) == 0:
            arr.append(i+1)

    if n == sum(arr):
        print(n,'=' ,end = ' ')
        for i in range(len(arr)):
            if i+1 == len(arr):
                print(arr[i], end='\n')
            else:
                print(arr[i],'+', end=' ')

    else:
        print(n,'is NOT perfect.')