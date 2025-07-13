bar = input()

stack = []
count = 0
prev = ''

for b in bar:
    if b == '(':
        stack.append('(')
    else:
        stack.pop()
        if prev == '(':  # 레이저
            count += len(stack)
        else:            # 쇠막대기 끝
            count += 1
    prev = b

print(count)
