def isPrime(check_range):
	if check_range == 1:
		return False
	
	n = int(check_range**0.5)
	for i in range(2, n+1):
		if check_range % i == 0:
			return False
	return True
	
# m, n = input().split()
# M, N = int(m), int(n)
# all_list = list(range(M, N+1))

M, N = map(int, input().split())

for i in range(M, N+1):
	if isPrime(i):
		print(i)
