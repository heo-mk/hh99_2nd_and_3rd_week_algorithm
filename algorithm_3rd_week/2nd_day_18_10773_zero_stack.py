import sys
input = sys.stdin.readline

K = int(input())
money_record = []
for i in range(K):
    money = int(input())
    if money == 0:
        if money_record:
            money_record.pop()
    else:
        money_record.append(money) 

print(sum(money_record))