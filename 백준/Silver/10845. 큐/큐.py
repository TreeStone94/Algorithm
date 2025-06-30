import sys

n = int(sys.stdin.readline())

queue = []

for _ in range(n):
    inCmd = sys.stdin.readline().split()

    cmd = inCmd[0]

    if cmd == 'push':
        queue.append(int(inCmd[1]))
    elif cmd == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.remove(queue[0])
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif cmd == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])