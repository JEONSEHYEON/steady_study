import sys
import math
sys.stdin = open("input.txt")

N = int(input())

for i in range(N):
    height , weight , value = map(int , input().split())
    y = value % height
    x = value // height + 1
    if y == 0:
        y = height
        x -= 1
    answer = y* 100 + x
    print(answer)