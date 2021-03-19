# 백준 11050 이항 계수

def bino(a, b):
	num1 = 1
	for i in range(a, a-b, -1):
		num1 = num1 * i
	num2 = 1
	for j in range(b, 1, -1):
		num2 = num2 * j
	return num1//num2


N, K = map(int, input().split())

print(bino(N,K))

# 이항계수
# 5,2 =>   5C2 // 2! => 5*4 // 2*1
# 15 3 => 15C3 // 3! => 15*14*13 // 3*2*1
