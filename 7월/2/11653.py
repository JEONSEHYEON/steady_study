import sys

sys.stdin = open("input.txt")

N = int(input())
i = 2
if N % i == 0:
    while N % i == 0:
        N = N // i
        print(i)
i += 1
while N != 1:
    if N % i == 0:
        N = N // i
        print(i)
    else:
        i += 2

