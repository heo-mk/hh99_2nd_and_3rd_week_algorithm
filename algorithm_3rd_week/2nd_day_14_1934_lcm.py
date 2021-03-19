import sys
input = sys.stdin.readline
from collections import deque

# 최대공약수 구하기
def gcd_euclid(a, b):
    if b == 0:
        return a
    return gcd_euclid(b, a%b)

# 최소공배수 구하는 공식
def lcm_easy(a, b):
    return (a * b)// gcd_euclid(a,b)

# # 최소공배수 구하기  # 되기는 하지만 시간 초과 
# def lcm(a, b):
#     q_a_multiples = deque()
#     q_b_multiples = deque()
#     for i in range(1, 45001):
#         q_a_multiples.append(a*i)
#         q_b_multiples.append(b*i)
        
#     while q_a_multiples:
#         a_pop = q_a_multiples.popleft()
#         if a_pop in q_b_multiples:
#             break
#     return a_pop


T = int(input())      # 테스트 횟수
for i in range(T):    # 테스트 횟수만큼 시행
    n, m = map(int, input().split()) 
    print(lcm_easy(n, m))

