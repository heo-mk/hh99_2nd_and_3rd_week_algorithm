T = int(input())
call_0_1 = {0:[1, 0], 1:[0,1]}  # dict를 이용한 memorization

# meomrization을 이용한 dynamic programming으로 피보나치 수열의 특정 항이 fibonacci의 0번과 1번 항을 몇 번 호출 했는가?
def fibo_0_1_cnt(n, fibo_calls):
    if n in fibo_calls:
        return fibo_calls[n]
    
    # memorization 부분
    nths_fibo = [x+y for x, y in zip(fibo_0_1_cnt(n-2, fibo_calls), fibo_0_1_cnt(n-1, fibo_calls))] 
    fibo_calls[n] = nths_fibo
    # print(nths_fibo)
    return nths_fibo

# print(fibo_0_1_cnt(3, call_0_1))

for n in range(T):
	inp = int(input())
	print(fibo_0_1_cnt(inp, call_0_1)[0], fibo_0_1_cnt(inp, call_0_1)[1])

