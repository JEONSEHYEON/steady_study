import sys

sys.stdin = open("input.txt")




def factor(x):
    if x == 0:
        return 1
    else:
        return x * factor(x - 1)


print(factor(int(input())))



    

