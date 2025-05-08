
for _ in range(10000):
    x,y = map(int, input().split())

    if x == 0 and y == 0:
        break

    if y % x == 0:
        print("factor")
    elif x / y == int(x/y):
        print("multiple")
    else:
        print("neither")