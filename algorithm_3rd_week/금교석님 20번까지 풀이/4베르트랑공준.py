def is_prime(N):
    if N<2:
        return False
    if N in (2,3):
        return True
    if N%2==0 or N%3==0:
        return False
    if N<10:
        return True
    
    k,L = 5,N**0.5
    while k<=L:
        if N%k==0 or N%(k+2)==0:
            return False
        k+=6
    return True

while True:
    N = int(input())
    if N==0:
        break
    cnt = 0
    for i in range(N+1,2*N+1):
        if is_prime(i):
            cnt+=1
    print(cnt)