import sys

sys.stdin = open('input.txt')

N = int(input())

k = list(map(int , input().split()))

s = sorted(set(k))

s = {s[i]:i for i in range(len(s))}

for i in k:
    print(s[i] , end=' ')