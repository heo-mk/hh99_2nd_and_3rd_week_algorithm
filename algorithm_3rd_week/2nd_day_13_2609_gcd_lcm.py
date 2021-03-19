from math import gcd
import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())   # 자연수 2개 입력.

# 최대공약수 구하기 : 일반적 알고리즘
def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

# 최대공약수 구하기 : 유클리드 알고리즘 = 재귀
def gcd_euclid(a, b):
    # a와 b의 최대공약수 = b와 a%b의 최대공약수
    if b == 0:
        return a
    return gcd_euclid(b, a%b)

# 최소공배수 구하기 : 백준에서 맞다고 나오긴 하지만 시간이 오래 걸림
def lcm(a, b):
    q_a_multiples = deque()
    q_b_multiples = deque()
    for i in range(1, 10001):
        q_a_multiples.append(a*i)
        q_b_multiples.append(b*i)
        
    while q_a_multiples:
        a_pop = q_a_multiples.popleft()
        if a_pop in q_b_multiples:
            break

    return a_pop

print(gcd_euclid(n, m))
print(lcm(n, m)) 


# 쉬운 풀이
def lcm_easy(a, b):
    return a * b // gcd_euclid(a,b)

def lcm_easy_more(a, b):
    return a * b // gcd(a,b)

print(gcd_euclid(n, m))
print(lcm_easy_more(n, m)) 



#### 백준 통과 코드 ####
from math import gcd
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) 

def gcd_euclid(a, b):
    if b == 0:
        return a
    return gcd_euclid(b, a%b)

def lcm_easy(a, b):
    return a*b//gcd(a,b)

print(gcd_euclid(n, m))
print(lcm_easy(n, m))  
