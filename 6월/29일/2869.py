import sys
import math

sys.stdin = open("input.txt")

up , down , height = map(int , input().split())
count = 0

print(math.ceil((height - up) / (up - down)) + 1)