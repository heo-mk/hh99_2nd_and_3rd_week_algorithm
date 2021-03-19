memo ={}
def nCr(n,r):
    key = str([n,r])
    if key in memo:
        return memo[key]
    
    if r ==0 or r==n:
        return 1
    memo[key] = nCr(n-1,r-1)+nCr(n-1,r)
    return memo[key]    

T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    print(nCr(K,N))