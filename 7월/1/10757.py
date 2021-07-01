import sys

sys.stdin = open("input.txt")

a , b = input().split()
if len(a) >= len(b):
    for i in range(len(a)):
        try:
            answer.append(a[i] + b[i])
        except:
            answer.append(a[i])
else:
    for i in range(len(b)):
        try:
            answer.append(a[i] + b[i])
        except:
            answer.append(b[i])
answer.reverse()
for i in answer:
    if i >= 10:
