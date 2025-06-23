n = int(input())

for _ in range(n):
    srr = list(input().split())
    for s in srr:
        for i in range(len(s)-1,-1, -1):
            print(s[i], end="")
        print(end=" ")