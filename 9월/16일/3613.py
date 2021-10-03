import sys

sys.stdin = open('input.txt')

c = input()
if '_' in c:
    s = list(c.split('_'))