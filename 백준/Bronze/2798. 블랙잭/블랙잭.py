from itertools import permutations

n, m = map(int,input().split())

arr = list(map(int,input().split()))
result = list(permutations(arr, 3))

max_ = 0
for perm in result:
    s = sum(perm)
    if s <= m and s > max_:
        max_ = s

print(max_)