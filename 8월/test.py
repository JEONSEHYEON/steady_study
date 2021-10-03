x1 , y1 , p1 , p2 = map(int , input().split())

if y1 >= x1:
    bias = p1 - p2
    for i in range(100):
        if (i*x1+bias) / y1 - int((i*x1+bias) / y1) == 0:
            print(x1*i + p1)
            break
    else:
        print(-1)
else:
    bias = p2 - p1
    for i in range(100):
        if (i*y1+bias) / x1 - int((i*y1+bias) / x1) == 0:
            print(y1*i + p2)
            break
    else:
        print(-1)




