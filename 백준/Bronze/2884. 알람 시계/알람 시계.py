h,m = map(int,input().split())

if h == 0:
    h = 24
    
a = h*60 + m - 45

h = a//60

if h == 24:
    h= 0
    
print(h, int(a%60))