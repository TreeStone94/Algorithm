numbers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()

n = n[::-1]
answer = 0
index = 0
for number in n:
    aa = [int(b)] * index
    x = 1
    for a in aa:
        x *= a

    if numbers.count(number) > 0:
        answer += (ord(number) - 55) * x
    else:
        answer += int(number) * x
    index += 1

print(answer)