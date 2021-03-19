import sys
input = sys.stdin.readline

# memoization하는 dict
cases = {1:1, 2:2}
def binary_cnt(n, memo):
    if n in memo:
        return memo[n]

    # memoization
    else:
        nth_cases = binary_cnt(n-2, memo) + binary_cnt(n-1, memo)
        remain = nth_cases % 15746  # 15746으로 나눈 나머지.
        memo[n] = remain
    return remain 

# 계산 시행
N = int(input())
print(binary_cnt(N, cases))

##################
import sys
input = sys.stdin.readline

# memoization하는 dict
cases = {1:1, 2:2}
def binary_cnt(n):
    if n in cases:
        return cases[n]

    # memoization
    else:
        nth_cases = binary_cnt(n-2) + binary_cnt(n-1)
        remain = nth_cases % 15746  # 15746으로 나눈 나머지.
        cases[n] = remain
    return remain 

N = int(input())
print(binary_cnt(N))