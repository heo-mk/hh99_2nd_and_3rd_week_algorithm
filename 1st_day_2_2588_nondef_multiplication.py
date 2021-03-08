a = int(input())  # 윗숫자   472
b = input()  # 아래숫자 385

b3 = int(b[0])  
b2 = int(b[1])
b1 = int(b[2])

result1 = a * b1
result2 = a * b2
result3 = a * b3

multiple = result3 * 100 + result2 * 10 + result1

print(result1)
print(result2)
print(result3)
print(multiple)