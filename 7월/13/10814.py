import sys

sys.stdin = open('input.txt')

N = int(input())
a = {}
for i in range(N):
    age , name = input().split()
    age = int(age)
    if age in a:
        a[age].append(name)
    else:
        a[age] = [name]
a = sorted(a.items())
for i in a:
    for j in i[1]:
        print(i[0] , j)