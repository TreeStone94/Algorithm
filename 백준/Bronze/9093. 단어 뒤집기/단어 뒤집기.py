n = int(input())

for _ in range(n):
    srr = list(input().split())
    for s in srr:
       print(s[::-1],end=" ")
