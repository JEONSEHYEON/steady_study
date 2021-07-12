import sys

sys.stdin = open("input.txt")
def check(st):
    if '666' in st:
        return 1
    else:
        return 0
N = int(input())
count = 0
num = 1
while N != count:
    if check(str(num)):
        count += 1
    num += 1

print(num - 1)