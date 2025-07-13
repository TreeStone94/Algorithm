n = int(input())
nums = list(map(int, input().split()))

count = {}
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

answer = [-1] * n
stack = []

for i in range(n):
    while stack and count[nums[stack[-1]]] < count[nums[i]]:
        idx = stack.pop()
        answer[idx] = nums[i]
    stack.append(i)

print(*answer)
