import sys

sys.stdin = open("input.txt")

N = int(input())
a = []
for i in range(N):
    x , y = map(int , input().split())
    a.append([x , y])
answer=[]
for x , y in a:
    count = 1
    for x1 , y1 in a:
        if x < x1 and y < y1:
            count += 1
    answer.append(count)

for i in answer:
    print(i , end= ' ')
    