import sys

sys.stdin = open("input.txt")
abc = 1
abc_list = list(int(input()) for _ in range(3))
for i in abc_list:
    abc *= i
abc = str(abc)
for i in range(10):
    i = str(i)
    print(abc.count(i))