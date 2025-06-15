import sys

# 입력 개수
N = int(sys.stdin.readline())

# 리스트에 입력값 저장
arr = [int(sys.stdin.readline()) for _ in range(N)]

for a in sorted(arr):
    print(a)
