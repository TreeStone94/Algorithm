a, b = list(map(str,input().split()))

ra = int(''.join(reversed(a)))
rb = int(''.join(reversed(b)))

if ra > rb:
    print(ra)
else:
    print(rb)