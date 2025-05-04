n = int(input())
n = 2**n


cnt = 0
for _ in range(n+1):
    cnt += 1*(n+1)

print(cnt)