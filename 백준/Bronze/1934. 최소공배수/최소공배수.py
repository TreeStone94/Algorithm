import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print((a * b) // g)
