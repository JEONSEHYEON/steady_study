import sys

sys.stdin = open('input.txt')

N = int(input())
a = {}
for i in range(N):
    x , y = map(int , input().split())
    if x in a:
        a[x].append(y)
    else:
        a[x] = [y]
a = sorted(a.items())
for i in a:
    i[1].sort()
for i in a:
    for j in i[1]:
        print(i[0] , j)
