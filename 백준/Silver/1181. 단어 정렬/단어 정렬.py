n = int(input())

s = []
for _ in range(n):
   t = input()
   l = [t, len(t)]
   s.append(l)

s = list(set(map(tuple, s)))

for a in sorted(s, key= lambda p: (p[1],p[0])):
    print(a[0])