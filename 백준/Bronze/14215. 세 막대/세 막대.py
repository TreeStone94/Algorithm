a, b, c = map(int, input().split())

arr = [a,b,c]
if a == b == c:
    print(a+b+c)
else:
    max_ = max(arr)
    s = sum(arr) - max_
    while max_ >= s:
        max_ -= 1
    print(max_ + s)