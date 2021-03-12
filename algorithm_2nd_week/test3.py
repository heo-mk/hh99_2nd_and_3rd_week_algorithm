# 6조 조상균의 코드
virus = [1] # 바이러스에 걸린 컴퓨터를 저장

def network(arr, virus):
        for com in arr: # 바이러스 걸린 컴퓨터와 연결된 컴퓨터 쌍으로 탐색
                if com[0] in virus: # 0번 컴퓨터가 바이러스에 걸렸다면
                        if com[1] not in virus: # 그리고 1번 컴퓨터는 아직 걸리지 않았다면
                                virus.append(com[1]) # 1번 컴퓨터를 감염 목록에 추가
                                network(arr, virus) # 1번 컴퓨터가 추가된 후 재귀 탐색
                elif com[1] in virus: # 위와 동일
                        if com[0] not in virus:
                                virus.append(com[0])
                                network(arr, virus)

# 입력
n = int(input())
m = int(input())
arr = list()
for _ in range(m):
        arr.append(list(map(int, input().split())))

#DFS
network(arr, virus)

print(len(virus) - 1) # 1번 컴퓨터 제외
