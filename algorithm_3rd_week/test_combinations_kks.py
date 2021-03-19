def DFS(L,res,ex):
    if L==M:
        print(res)
        return
    for i in range(ex+1,N+1):
        DFS(L+1,res+str(i)+" ",i)


N,M = map(int,input().split())
DFS(0,"",0)