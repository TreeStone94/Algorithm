a = []

for _ in range(5):
    x = list(input())
    a.append(x)

answer = ''

for i in range(15):
    for j in range(5):
        try:
            answer += a[j][i]
        except IndexError:
            continue

print(answer)