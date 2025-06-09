a = '666'

n = int(input())
cnt = 0

range_ = 666
while cnt != n:
    if str(range_).find(a) > -1:
        cnt +=1
    range_ +=1

print(range_-1)