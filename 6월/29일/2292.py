
import sys

sys.stdin = open("input.txt")

N = int(input())
count = 0
x = 1
count = 1
while True:
    if N <= x:
        print(count)
        break
    else:
        x = x + 6 *(count)
        count += 1



