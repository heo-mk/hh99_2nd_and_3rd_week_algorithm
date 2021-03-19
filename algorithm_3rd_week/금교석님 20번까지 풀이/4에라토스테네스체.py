limit = 123456*2
prime = [False]*(limit+1)

for i in range(2,int(limit**0.5)+1):
    if prime[i]==False:
        for j in range(i*2,limit+1,i):
            prime[j] =True

while True:
    N = int(input())
    if N ==0:
        break
    count = 0
    for v in prime[N+1:2*N+1]:
        if v == False: #소수이면
            count+=1
    print(count)