aArr = [0 for _ in range(30)]

for _ in range(28):
    i = int(input())
    aArr[i-1] = i

for i in range(30):
    if aArr[i] == 0:
        print(i+1)