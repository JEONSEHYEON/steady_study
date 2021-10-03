import sys

sys.stdin = open('input.txt')

N , M = map(int , input().split())
ans = 1
div = 1
if M != 0:
    for i in range(N - M + 1, N + 1):
        ans *= i

    for i in range(1 , M + 1 ):
        div *= i
    print(ans // div)

else:
    print(1)