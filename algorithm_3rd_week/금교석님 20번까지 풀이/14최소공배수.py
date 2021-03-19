N = int(input())

def GCD(a,b):
    G,D = max(a,b),min(a,b)
    while D>0:
        G=G%D  
        G,D =D,G  
    return G*(a//G)*(b//G)

for _ in range(N):
    a,b = map(int,input().split())
    print(GCD(a,b))
    