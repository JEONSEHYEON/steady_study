import sys

sys.stdin = open('input.txt')

N = int(input())

if N % 2:
    for _ in range(N // 2):
        print(1 , 2, end=' ')
    print(3)
else:
    for _ in range(N // 2):
        print(1 , 2, end=' ')
