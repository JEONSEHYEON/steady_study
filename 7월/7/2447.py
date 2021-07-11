def printer(x ):
    if x == 3:
        return ('*' * 3 ,
                '*'*1,' '*1 , '*'*1 ,
                '*' * 3)
    else:
        a = printer(x//3)
        a1 = a * 3
        a2 = a* (x//3)
        kong = ' ' * x // 3
        return 

print(printer(3))