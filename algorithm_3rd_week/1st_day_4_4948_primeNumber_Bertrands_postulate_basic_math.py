import sys
input = sys.stdin.readline

# 소수 판별, 2 이상 모든 정수의 소수 여부 판별이 가능
def isPrime(check_range):
    if check_range == 1:
        return False
    
    n = int(check_range**0.5)
    for i in range(2, n+1):
        if check_range % i == 0:
            return False
    return True

# 범위 내 소수 갯수 출력
while True:
    M = int(input())
    if M == 0:
        break
    
    primes = []
    for i in range(M+1, 2*M+1):
        if isPrime(i):
            primes.append(i)
    
    print(primes)
    print(len(primes))
