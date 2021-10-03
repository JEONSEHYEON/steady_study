import sys


sys.stdin = open('input.txt')
input = sys.stdin.readline
x , y , z , total = map(int , input().split())

def hamsu():
    for i in range(total // x + 1):
        for j in range(total // y + 1):
            for k in range(total // z + 1):
                if i * x + j * y + k * z == total:
                    return 1
    return 0

if hamsu():
    print(1)
else:
    print(0)