s = input()

a = ""
for i in range(len(s),0,-1):
    a += s[i-1]

if s == a:
    print(1)
else:
    print(0)