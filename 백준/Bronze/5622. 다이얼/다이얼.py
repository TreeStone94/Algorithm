a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

n = input()

sum = 0
for x in n:
    for i in range(len(a)):
       if x in a[i]:
           sum += i + 3


print(sum)
