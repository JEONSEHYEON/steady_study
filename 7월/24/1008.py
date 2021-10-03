import sys

sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    pibo = [[1 , 0] , [0 , 1]]
    num = int(input())
    if num < 2:
        print(pibo[num][0] , pibo[num][1])
    else:
        for j in range(2 , num + 1):
            pibo.append([pibo[j - 1][0] + pibo[j - 2][0] ,pibo[j - 1][1] + pibo[j - 2][1]])
        print(pibo[-1][0] , pibo[-1][1])

