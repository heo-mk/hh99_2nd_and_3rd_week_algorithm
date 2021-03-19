import sys
sys.stdin = open('a.txt','rt')

N,K = map(int,input().split())

# 초기화
coins =[]
for _ in range(N):
    coin = int(input())
    coins.append(coin)

#시작 인덱스 찾기
start_idx =0
for idx,coin in enumerate(coins):
    if K<coin:
        start_idx = idx-1
        break
else:
    start_idx = len(coins)-1 # 못찾았으면 마지막 인덱스 


result = 0
while start_idx>=0 and K>0:
    result+=K//coins[start_idx]
    K = K%coins[start_idx]
    start_idx-=1
    
print(result)
    
    


