n = int(input())


if n == 0:
    print(0)
else:
    answer = 0
    m = 1
    for i in range(n):
        m *= (i+1)
    m = list(str(m))
    for i in range(len(m)-1,-1,-1):
        if m[i] == '0':
            answer +=1
        else:
            break
    print(answer)