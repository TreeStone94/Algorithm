p = int(input())
n = int(input())

pa = []
for _ in range(n):
    x, y = map(int, input().split())
    pa.append(x * y)

if p == sum(pa):
    print('Yes')
else:
    print('No')