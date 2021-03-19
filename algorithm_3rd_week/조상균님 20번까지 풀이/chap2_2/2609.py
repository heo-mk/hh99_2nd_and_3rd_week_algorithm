# 백준 2609 최대공약수와 최소공배수
def gcd(m, n):
	if m > n:  # 항상 n이 더 크게
		m, n = n, m
	while m % n != 0:  # 유클리드 호제법
		a = m % n
		m = n
		n = a
	return n

m, n = map(int, input().split())
gcd = gcd(m,n)
lcm = m * n // gcd

print(gcd)
print(lcm)
