import sys

arr = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    arr.append(n)


m = max(arr)
prime = [True] * (m+1)
prime[0] = prime[1] = False

for i in range(2, m+1):
    if prime[i]:
        for j in range(i*i, m+1, i):
            prime[j] = False
    if i % 2 == 0:
        prime[i] = False

for a in arr:
    wrong = True
    for i in range(3,a//2+1,2):
        if prime[i] and prime[a-i]:
            wrong = False
            print(a,'=',i,'+', a-i)
            break

    if wrong:
        print("Goldbach's conjecture is wrong.")



