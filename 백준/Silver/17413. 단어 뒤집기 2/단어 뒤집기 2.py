stack = []
s = input()

isTag = False
for ch in s:
    if ch == '<' :
        while stack:
            print(stack.pop(), end="")
        isTag = True
        print(ch,end="")
    elif ch == '>':
        isTag = False
        print(ch, end="")
    elif isTag:
        print(ch, end="")
    elif ch == " ":
        while stack:
            print(stack.pop(), end="")
        print(end= " ")
    else:
        stack.append(ch)

while stack:
    print(stack.pop(), end="")