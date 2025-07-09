import sys

leftStack = list(sys.stdin.readline().strip())
rightStack = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    cmd = sys.stdin.readline().split()


    if cmd[0] == 'L' and leftStack:
        s = leftStack.pop()
        rightStack.append(s)
    elif cmd[0] == 'D' and rightStack:
        s = rightStack.pop()
        leftStack.append(s)
    elif cmd[0] == 'B' and leftStack:
        leftStack.pop()
    elif cmd[0] == 'P':
        leftStack.append(cmd[1])

    # yxz
    #
print("".join(leftStack), end="")

while rightStack:
    print(rightStack.pop(), end="")