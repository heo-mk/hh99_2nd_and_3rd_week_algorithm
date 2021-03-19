# 백준 1010 다리 놓기

# 이항계수 활용
def bino(a, b):
	num1 = 1
	for i in range(a, a-b, -1):
		num1 = num1 * i
	num2 = 1
	for j in range(b, 1, -1):
		num2 = num2 * j
	return num1//num2

#입력
n = int(input())
result = []
for i in range(n):
	x, y = map(int, input().split())
	if x < y:
		x, y = y, x
	result.append(bino(x,y))

for r in result:
	print(r)
