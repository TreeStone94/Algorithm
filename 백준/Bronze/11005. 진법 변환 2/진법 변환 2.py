ap = {i: str(i) for i in range(10)}
ap.update({i: chr(55 + i) for i in range(10, 36)})

n, b = map(int, input().split())

answer = ''
while n > 0:
    answer = ap[n % b] + answer
    n //= b

print(answer)
