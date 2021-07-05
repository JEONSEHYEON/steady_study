import sys
from math import pi

sys.stdin = open("input.txt")
N = float(input())

print('%6f' %(N * N * pi))
print( '%6f' %((N + N) * (N + N) / 2))

