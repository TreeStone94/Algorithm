a = []

for _ in range(5):
    x = list(input())
    a.append(x)

answer = ''

for i in range(15):
    for j in range(5):
        if i < len(a[j]):
            answer += a[j][i]

print(answer)