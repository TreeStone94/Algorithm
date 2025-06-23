import sys
n = int(input())

arr = []

def empty(arr):
    if len(arr) == 0:
        return True
    else:
        return False

for _ in range(n):
    a = list(sys.stdin.readline().split())

    cmd = a[0]
    if cmd == 'push':
        arr.append(int(a[1]))
    elif cmd == 'pop':
        if empty(arr):
            print(-1)
        else:
            print(arr.pop())
    elif cmd == 'size':
        print(len(arr))
    elif cmd == 'empty':
        if empty(arr):
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if empty(arr):
            print(-1)
        else:
            print(arr[len(arr)-1])

