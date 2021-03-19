import sys
input = sys.stdin.readline

T = int(input())  

# factorial 재귀 함수
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

# binomial coefficent == n!/r!*(n-r)!
def binomial_coefficient(n, r):
    binomial_coeffi = factorial(n)/(factorial(r)*factorial(n-r))
    return binomial_coeffi

for i in range(T):
    west_sites, east_sites = map(int, input().split())
    max_bridges = binomial_coefficient(east_sites, west_sites)
    print(int(max_bridges))