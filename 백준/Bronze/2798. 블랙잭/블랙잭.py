from itertools import combinations

n,m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for a in list(combinations(arr,3)):
    if sum(a) > m:
        continue
    else:
        result.append(a)

print(sum(max(result)))
