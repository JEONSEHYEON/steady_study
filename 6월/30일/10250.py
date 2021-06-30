import sys

sys.stdin = open("input.txt")

N = int(input())

for i in range(N):
    height , weight , value = map(int , input().split())
    y = value % height
    if y == 0:
        y = height
    x = value // height
    answer = y* 100 + x + 1
    print(answer)