x,y,z = map(int, input().split())


if x == y and x == z:
    print(10000 + x * 1000)
elif x == z or x == y:
    print(1000 + x*100)
elif z == y:
    print(1000 + z*100)
else:
    print(max(x,z,y) * 100)
