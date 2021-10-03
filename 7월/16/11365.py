import sys

sys.stdin = open('input.txt')
while True:
    s = input()
    if s == 'END':
        break
    print(s[::-1])
