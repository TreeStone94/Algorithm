aArr = []

for _ in range(10):
    i = int(input())
    x = i % 42
    if aArr.count(x) == 0:
        aArr.append(x)

print(len(aArr))