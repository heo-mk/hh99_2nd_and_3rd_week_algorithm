# input = 100

# def fibo_recursion(n):
# 	if n <= 2:
# 		return 1

# 	return fibo_recursion(n-1) + fibo_recursion(n-2)

# print(fibo_recursion(input))

input = 100

memo = {1:1, 2:1}

def fibo_dp(n: int, fibo_memo: dict):
	if n in fibo_memo:
		return fibo_memo[n]

	nth_fibo = fibo_dp(n-1, fibo_memo) + fibo_dp(n-2, fibo_memo)	
	fibo_memo[n] = nth_fibo	
	return nth_fibo

print(fibo_dp(input, memo))

