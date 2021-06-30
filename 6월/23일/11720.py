import sys

sys.stdin = open("input.txt")

N = int(input())
str1 = input()
hap = 0
for i in str1:
    hap += int(i)
print(hap)