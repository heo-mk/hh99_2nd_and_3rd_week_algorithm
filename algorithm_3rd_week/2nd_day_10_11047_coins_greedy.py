import sys
input = sys.stdin.readline
N, K = map(int, input().split())

coin_values = []
for i in range(N):
    coin_values.append(int(input().rstrip()))

coin_values.sort(reverse=True)
print(coin_values)

coin_cnt = []
def coin_cnt_cal(value_list, total_money):
    for j in range(len(value_list)):
        if value_list[j] <= total_money:
            coin_cnt.append(total_money//value_list[j])
            remain = total_money%value_list[j]
            print(coin_cnt)
            if remain == 0:
                break
            else:
                total_money = remain
                print(total_money)
    print(coin_cnt)            
    return sum(coin_cnt) 

print(coin_cnt_cal(coin_values, K))