import sys
sys.stdin = open('a.txt','rt')

# MAP 만들기
MAP =[]
N = int(input())
for _ in range(N):
    house = list(map(int,input().split()))
    MAP.append(house)

for i in range(1,N):
    for j in range(3):
        left = (j+1)%3   
        right = (j+2)%3  
        MAP[i][j] += min(MAP[i-1][left],MAP[i-1][right])
print(min(MAP[N-1]))
