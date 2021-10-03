import sys

sys.stdin = open('input.txt')

s = input()
t = input()

if len(s) < len(t):
    short = len(s)
    check = t[:short]
    if check == s:
        print(1)
    else:
        print(0)

elif len(t) >= len(s):
    short = len(t)
    check = s[:short]
    if check == t:
        print(1)
    else:
        print(0)