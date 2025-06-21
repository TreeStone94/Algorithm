n = int(input())

xs = list(map(int, input().split()))

xi = list(sorted(set(xs)))

dic = {}
for i in range(len(xi)):
    dic[xi[i]] = i

for x in xs:
    print(dic[x], end=" ")