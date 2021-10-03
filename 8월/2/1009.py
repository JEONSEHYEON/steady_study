import sys

sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    a , b = map(int , input().split())
    ans = 1
    for j in range(b):
        ans = ans * a
        ans %= 10
    if ans == 0:
        print(10)
    else:
        print(ans)