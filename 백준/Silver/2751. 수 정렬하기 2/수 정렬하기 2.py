import sys

n = int(input())

arr = [int(sys.stdin.readline()) for _ in range(n)]

for a in sorted(arr):
    print(a)