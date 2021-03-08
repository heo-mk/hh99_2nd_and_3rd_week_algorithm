num = _1st_num = int(input())
count = 0

while True:
    td = num // 10
    sd = num % 10
    temp = td + sd
    new_sd = temp % 10
    
    num = (sd * 10) + new_sd

    count += 1

    if _1st_num == num:
        break

print(count)