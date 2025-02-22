x,y = map(int, input().split())
z = int(input())

x += z // 60
y += z % 60



if y >= 60:
    y -= 60
    x +=1


if x >= 24:
    x -= 24

print(x,y)