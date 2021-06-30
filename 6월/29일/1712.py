import sys

sys.stdin = open("input.txt")

fix , flex , made = map(int , input().split())


if made - flex <= 0:
    print(-1)
else:
    print(fix // (made - flex) + 1)
