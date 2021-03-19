import sys
sys.setrecursionlimit(5000)

def DFS(L,res):
    if res<=0:
        if res==0:
            print(L)
            exit(0)
        return
    DFS(L+1,res-5)
    DFS(L+1,res-3)
    
N =int(input())
DFS(0,N)
print(-1)
