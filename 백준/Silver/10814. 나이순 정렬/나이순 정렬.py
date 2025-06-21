n = int(input())

s = []
i = 0
for _ in range(n):
   age, name = input().split()
   s.append((int(age),name,i))
   i += 1

for a in sorted(s, key= lambda p: (p[0],p[2])):
    print(a[0],a[1])