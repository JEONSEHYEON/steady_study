import sys

sys.stdin = open('input.txt')

so = [2 for _ in range(10)]
count = 0

N = int(input())

for i in range(N):
    a , b = map(int, input())
    