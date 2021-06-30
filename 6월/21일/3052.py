import sys

sys.stdin = open("input.txt")

a = list(map(int , sys.stdin.readlines()))
answer = []
for i in a:
    answer.append(i % 42)

print(len(set(answer)))


