s = input().lower()
a = list(set(s))
cnt = []


for x in a:
    cnt.append(s.count(x))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(a[cnt.index(max(cnt))].upper())