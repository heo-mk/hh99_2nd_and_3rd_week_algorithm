import sys
input = sys.stdin.readline
t, p = map(int, input().split())

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

# binomial coefficent == n!/r!*(n-r)!
def binomial_coefficient(n, r):
    binomial_coeffi = factorial(n)/(factorial(r)*factorial(n-r))
    return binomial_coeffi

print(int(binomial_coefficient(t, p)))

nCr 
(a+b)^n : n!/r!(n-r)!