import sys

sys.stdin = open("input.txt")

a , b = map(int , input().split())

if b - 45 < 0:
    b += 15
    if a - 1 < 0:
        a = 23
    else:
        a -= 1
else:
    b -= 45

print(a , b)