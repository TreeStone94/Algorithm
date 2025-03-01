amount = int(input())
cnt = int(input())

compareAmount = 0

for _ in range(cnt):
    x,z = map(int, input().split())
    compareAmount += x*z


if amount == compareAmount:
    print("Yes")
else:
    print("No")