import sys

cnt = int(input())

for i in range(cnt):
    x,y = map(int,sys.stdin.readline().split())
    print("Case #"+str(i+1)+":",x+y)