arr = []

count = 0

a = int(input())
arr.append(a)

b = int(input())
count = arr.count(b)
arr.append(b)

c = int(input())
count = arr.count(c)
arr.append(c)

sum = sum(arr)

if arr.count(60) == 3:
    print('Equilateral')
elif sum == 180 and count == 1:
    print('Isosceles')
elif sum == 180 and count == 0:
    print('Scalene')
else:
    print('Error')