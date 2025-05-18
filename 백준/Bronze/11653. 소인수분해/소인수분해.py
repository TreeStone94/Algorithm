n = int(input())
num = 2

while n != 1:
    if n % num == 0:
        print(num)
        n = n // num
        num = 2
    else:
        num +=1