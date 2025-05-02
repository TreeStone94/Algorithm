ap = {str(i): i for i in range(10)}
ap.update({chr(55 + i): i for i in range(10, 36)})


n, b = input().split()
n = n[::-1]

answer = 0
for i in range(len(n)):
    answer += ap[n[i]] * int(b) ** i

print(answer)
