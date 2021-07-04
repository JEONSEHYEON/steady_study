import sys

sys.stdin = open("input.txt")

while True:
    a , b , c = map(int , input().split())
    if a == 0 and b == 0 and c == 0:
        break
    abc_max = max(a , b ,c) ** 2
    if abc_max == a ** 2 + b ** 2 + c ** 2 - abc_max:
        print('right')
    else:
        print('wrong')
        