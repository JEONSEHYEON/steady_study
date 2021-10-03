import sys

sys.stdin = open('input.txt')

cash = int(input())   ## 주어진 현금

stocks = list(map(int , input().split()))   ##주식 정보


##준현이
def junhyeon(money , stocks):
    last = stocks[-1]
    hold = 0
    for stock in stocks:
        if money == 0:
            break
        share = (money // stock)
        money -= (share * stock)
        hold += share
    return money + (hold * last)

## 성민이
def sengmin(money , stocks):
    hold = 0
    last = stocks[-1]
    for i in range(3 , len(stocks)):
        if stocks[i] < stocks[i - 1] < stocks[i - 2] < stocks[i - 3]: #100  10 20 23 34 55 30 22 19 12 45 23 44 34 38
            share = (money // stocks[i])
            money -= (share * stocks[i])
            hold += share
        elif stocks[i] > stocks[i - 1] > stocks[i - 2] < stocks[i - 3]:
            money += (hold * stocks[i])
            hold = 0
    return money + (hold * last)

a = junhyeon(cash , stocks)
b = sengmin(cash , stocks)
if a < b:
    print('TIMING')
elif a == b:
    print('SAMESAME')
else:
    print('BNP')