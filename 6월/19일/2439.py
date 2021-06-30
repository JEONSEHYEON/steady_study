import sys

sys.stdin = open("input.txt")
N = int(input())

for i in range(1 , N + 1):
    empty = ' ' * (N - i)
    star = '*' * i
    print(empty + star)

