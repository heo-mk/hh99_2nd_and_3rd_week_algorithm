import sys
input = sys.stdin.readline

N1 = int(input())                      # 숫자 카드 갯수
C1 = list(map(int, input().split()))   # 숫자 카드에 적힌 정수
C1.sort()                              # 이분탐색을 위한 오름차순 정렬 
print(C1)
print()

N2 = int(input())                      # N1과 맞춰볼 숫자 카드 갯수
C2 = list(map(int, input().split()))     # N1의 카드의 숫자와 일치하는지 확인하는 부분

# 이분정렬 
for i in range(N2): # N2 갯수만큼 탐색을 해야 하니까
    start = 0
    end = N1 -1
    determinator = 0
    
    while start <= end:
        mid = (start + end)//2
        if C2[i] == C1[mid]:
            determinator = 1
            break
        elif C2[i] > C1[mid]:
            start = mid + 1
        else:
            end = mid - 1
    print(1, end=' ') if determinator else print(0, end=' ')