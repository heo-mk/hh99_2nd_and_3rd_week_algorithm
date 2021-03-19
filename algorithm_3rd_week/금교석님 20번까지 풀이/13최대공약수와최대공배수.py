#유클리드 호제법
A,B = map(int,input().split())
G,D = max(A,B),min(A,B)
while D>0:
    G=G%D  
    G,D =D,G 

print(G)
print(G*(A//G)*(B//G)) 
    