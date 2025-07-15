a, b = map(int,input().split())

# 최대 공약수 (최대공약수는 두 개 이상의 자연수의 공통된 약수 중 가장 큰 수를 말합니다.)
# 최소 공배수 (최소공배수는 두 개 이상의 자연수의 공통 배수 중 가장 작은 수입니다. )

n = (a*b)
number = 2
arr = []
while min(a,b) >= number:

    if a % number == 0 and b % number == 0:
        arr.append(number)
        a = a//number
        b = b//number
    else:
        number +=1

m = 1
for ar in arr:
    m *= ar

print(m)
print(n//m)


