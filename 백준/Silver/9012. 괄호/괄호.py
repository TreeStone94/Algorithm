
n = int(input())
for _ in range(n):
    arr = list(input())
    stack = []

    valid = True
    for a in arr:
        if a == '(':
            stack.append(a)
        else:
            if not stack:
                valid =False
            else:
                stack.pop()

    if len(stack) != 0 or valid == False:
        print('NO')
    else:
        print('YES')

