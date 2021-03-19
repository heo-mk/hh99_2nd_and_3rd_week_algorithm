# 1934 최소공배수

def gcd(m, n):
	if m > n:  # 항상 n이 더 크게
		m, n = n, m
	while m % n != 0:  # 유클리드 호제법
		a = m % n
		m = n
		n = a
	return n

n = int(input())
arr = []
for i in range(n):
	m, n = map(int, input().split())
	arr.append((m * n) // gcd(m, n))

for result in arr:
	print(result)
