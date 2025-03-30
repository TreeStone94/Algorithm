import sys

cnt = int(input())

for _ in range(cnt):
    x,y = map(int,sys.stdin.readline().split())
    print(x+y)