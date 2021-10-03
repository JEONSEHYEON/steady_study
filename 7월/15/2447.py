import sys

def rec(N):
    if N == 3:
        star[0][0:3] = star[2][0:3] = [1] *3
        star[1][0:3] = [1 , 0 , 1]
    else:
        a = N // 3
        rec(a)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                for k in range(a):
                    star[a*i + k][j*a:a*(j+1)] = star[k][ : a]
        

sys.stdin = open('input.txt')

N = int(input())

star = [[0 for _ in range(N)] for _ in range(N)]

rec(N)
for i in star:
    for j in i:
        if j == 1:
            print('*' , end='')
        else:
            print(' ' , end='')
    print()

