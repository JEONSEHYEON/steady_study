import sys


def numplus(num):
    hap = 0
    while num:
        a = num % 10
        b = num // 10
        hap += a
        num = b
    return hap

def ret(num):
    return num % 10

def connect(a , b):
    return a * 10 + b

def find(num):
    fixnum = num
    count = 0
    while True:
        hap = numplus(num)
        a = ret(num)
        b = ret(hap)
        count += 1
        if fixnum == connect(a , b):
            print(count)
            break
        else:
            num = connect(a , b)
            

sys.stdin = open("input.txt")
N = int(input())
find(N)