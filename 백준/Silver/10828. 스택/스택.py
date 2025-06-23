import sys
n = int(input())

arr = []

for _ in range(n):
    a = sys.stdin.readline().split()

    cmd = a[0]
    if cmd == 'push':
        arr.append(int(a[1]))
    elif cmd == 'pop':
        if not arr:
            print(-1)
        else:
            print(arr.pop())
    elif cmd == 'size':
        print(len(arr))
    elif cmd == 'empty':
        if not arr:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if not arr:
            print(-1)
        else:
            print(arr[-1])

