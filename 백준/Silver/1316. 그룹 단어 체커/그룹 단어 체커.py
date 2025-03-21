n = int(input())

cnt = 0
for _ in range(n):
    s = input()
    hasGroup = True
    for x in set(s):
        if s.count(x) > 1 and s.find(x*s.count(x)) == -1:
            hasGroup = False
    if hasGroup:
        cnt += 1


print(cnt)