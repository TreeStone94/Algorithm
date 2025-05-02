n = int(input())

price = [25, 10, 5, 1]

arr = []
for _ in range(n):
    c = int(input())
    arr.append(c)


for a in arr:
    for p in price:
        print(a // p, end=' ')
        a = a%p
    print()