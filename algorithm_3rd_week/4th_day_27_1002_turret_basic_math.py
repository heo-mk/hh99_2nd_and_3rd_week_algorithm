# 내 풀이 : 복잡
# import sys
# input = sys.stdin.readline
# from math import sqrt

# T = int(input())
# for i in range(T):
#     coordinates_info = input().split()  # x1, y1, r1, x2, y2, r2
#     # print(cooridnates_info)
#     x1 = int(coordinates_info[0]); y1 = int(coordinates_info[1]); r1 = int(coordinates_info[2])
#     x2 = int(coordinates_info[3]); y2 = int(coordinates_info[4]); r2 = int(coordinates_info[5])
#     distance_btw_two_turrets = sqrt((x1 - x2)**2 + (y1 - y2)**2)  # 두 터렛 사이의 거리
#     sum_r1_r2 = r1 + r2  # 두 터렛에서 각각 측정한 목표 지점까지 거리의 합
#     gap_r1_r2 = abs(r1-r2)
    
#     # 두 터렛이 같은 위치
#     if x1 == x2 and y1 == y2: 
#         if gap_r1_r2 == 0:  # 두 터렛에서 거리도 같다 : 원둘레 어느 곳에도 가능 = 위치는 무한대
#             print(-1)
#         else:               # 반지름이 다른 동심원 2개 : 불가능한 상황 
#             print(0)
#     # 두 터렛이 서로 다른 위치
#     else:
#         if sum_r1_r2 > distance_btw_two_turrets:  
#             print(2)   # 접점이 두개
#         elif sum_r1_r2 == distance_btw_two_turrets:
#             print(1)   # 접점이 한개
#         elif sum_r1_r2 < distance_btw_two_turrets:
#             print(0)   # 접점이 있을 수 없다 = 불가능한 상황


# 두 원이 서로 만나고 만나지 않는 조건에 따라 출력 정하기
# 모든 경우를 합리적으로 담은 풀이
from math import sqrt
T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance_btw_origins = sqrt((x1-x2)**2 + (y1-y2)**2)
    radius_and_distance = [r1, r2, distance_btw_origins]
    longest = max(radius_and_distance)
    radius_and_distance.remove(longest)
    
    # 두 터렛이 같은 위치 = 두 터렛을 중심으로 하는 원이 같은 원이라 일치
    if distance_btw_origins == 0 and r1 == r2:
        print(-1)    
    # 두 터렛이 다른 곳에 있으면서 두 원이 서로 접할 때. 외접 내접 모두 포함
    elif longest == sum(radius_and_distance):  # 이 조건은 distance_btw_origins == r1 + r2 도 포함
        print(1)
    # 두 터렛이 다른 곳에 있으면서 두원이 서로 접하지 않을 때. 두 원이 서로 남남 
    elif longest > sum(radius_and_distance):
        print(0)
    # 앞서 특수한 경우들 모두 다루고, 마지막 경우에는 모든 경우를 몰아 넣는다.
    else:
        print(2)