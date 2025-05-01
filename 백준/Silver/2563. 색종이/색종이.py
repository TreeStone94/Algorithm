n = int(input())

paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x,y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += paper[k].count(1)  # 1 개수만 세어준다

print(result)
