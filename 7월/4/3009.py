import sys

answer = [[] , []]
sys.stdin = open("input.txt")
def Scale(a):
    if a[0] == a[1]:
        return a[2]
    elif a[0] == a[2]:
        return a[1]
    else:
        return a[0]
for i in range(3):
    a , b = map(int , input().split())
    answer[0].append(a)
    answer[1].append(b)

print(Scale(answer[0]) , Scale(answer[1]))

