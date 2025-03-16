c = [1,1,2,2,2,8]

n = list(map(int, input().split()))

for i in range(len(n)):
    n[i] = c[i] - n[i]
    print(n[i], end=" ")