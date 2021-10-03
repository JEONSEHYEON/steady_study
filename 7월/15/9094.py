import sys

sys.stdin = open("input.txt")

def check(n , m):
    count = 0
    for i in range(1 , n - 1):
        for j in range(i + 1, n):
            if not (i**2 + j**2 + m) % (i*j):
                count += 1
    return count

num = int(input())

for i in range(num):
    n , m = map(int , input().split())
    print(check(n , m))
    