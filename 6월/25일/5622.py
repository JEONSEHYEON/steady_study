import sys

sys.stdin = open("input.txt")
dial = ['' , '' , '1' ,'ABC' , 'DEF' , 'GHI' , 'JKL' ,'MNO' , 'PQRS' , 'TUV' , 'WXYZ' ]
s = input()
sum = 0
for i in s:
    for j in dial:
        if i in j:
            sum += dial.index(j)
            break
print(sum)
