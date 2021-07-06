import sys

sys.stdin = open('input.txt')

N = int(input())
for i in range(N):
    x1 , y1 , r1 , x2 , y2 , r2 = map(int , input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
    r = abs(r1 - r2)
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d < r1 + r2 and d > r:
            print(2)
        elif d == r1 + r2 or d == r:
            print(1)
        else:
            print(0)
