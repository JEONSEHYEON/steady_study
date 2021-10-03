import sys

sys.stdin = open('input.txt')

a = int(input())

for i in range(a):
    n , m = map(int , input().split())
    for j in range(m):
        a , b = map(int , input().split())
    print(n - 1)