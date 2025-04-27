a = []

for _ in range(9):
    x = list(map(int, input().split()))
    a.append(x)

maxNum = max(map(max,a))
print(maxNum)

for i in range(9):
    for j in range(9):
        if a[i][j] == maxNum:
            print(i+1,j+1)
            break