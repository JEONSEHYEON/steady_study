import sys

sys.stdin = open("input.txt")
a = []
while True:
    try:
        num = int(input())
        a.append(num)
    except:
        break
print(max(a))
print(a.index(max(a)) + 1)
