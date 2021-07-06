import sys

sys.stdin = open("input.txt")

def pibo(x , y , count):
    if count == 0:
        return x
    else:
        count -= 1
        return pibo(y , x + y , count)

N = int(input())

print(pibo(0 , 1 , N))