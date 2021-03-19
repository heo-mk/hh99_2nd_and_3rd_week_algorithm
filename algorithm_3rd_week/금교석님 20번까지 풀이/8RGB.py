import sys
sys.stdin = open('a.txt','rt')

# MAP 만들기
MAP =[]
N = int(input())
for _ in range(N):
    house = list(map(int,input().split()))
    MAP.append(house)

G_min = float('inf')
def DFS(L,res,check):
    global G_min
    if res > G_min:
        return
    if L==N:
        G_min = min(G_min,res)
        return

    for i in range(3):
        if i!=check:
            DFS(L+1,res+MAP[L][i],i)
DFS(0,0,-1)
print(G_min)
        