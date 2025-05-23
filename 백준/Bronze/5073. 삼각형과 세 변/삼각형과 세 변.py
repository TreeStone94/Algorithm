while True:
    x, y, z = map(int,input().split())
    arr = [x,y,z]

    if x == 0 and y == 0 and z == 0:
        break

    if sum(arr) - max(arr) <= max(arr):
        print('Invalid')
    elif arr.count(x) == 3:
        print('Equilateral')
    elif arr.count(x) == 2 or arr.count(y) == 2 or arr.count(z) == 2:
        print('Isosceles')
    else:
        print('Scalene')