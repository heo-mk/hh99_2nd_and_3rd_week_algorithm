# f(2) = 2 x f(1) + 1 = 2 x 1 + 1 = 3
# print(hanoi_tower(3))    # f(3) = 2 x f(2) + 1 = 2 x 3 + 1 = 7
# print(hanoi_tower(4))    # f(4) = 2 x f(3) + 1 = 2 x 7 + 1 = 15
# print(hanoi_tower(5))    # f(5) = 2 x f(4) + 1 = 2 x 15 + 1 = 31
# print(hanoi_tower(6))
# print(hanoi_tower(10)) 


# # Disk movement
# N = int(input())
# # _1st = 1   # starting pole
# # _2nd = 2   # middle pole
# # _3rd = 3   # end pole
# def hanoi_tower_move(N, _1st, _3rd, _2nd):
#     if N == 1:
#         print(_1st, _3rd)
#         return 
    
#     # recursion : n-1 disks move to 2nd pole
#     hanoi_tower_move(N-1, _1st, _2nd, _3rd)
#     # move the biggest one to 3rd_pole
#     print(_1st, _3rd)
#     # move n-1 disks in 2nd_pole to 3rd_pole
#     hanoi_tower_move(N-1, _2nd, _3rd, _1st)
    
# print(hanoi_tower_move(N, 1, 3, 2))

# total number of disk move, baekjoon 1914, 11729
def hanoi_tower(n):
    if n <= 1:
        return 1
    return 2*hanoi_tower(n-1) + 1   # 점화식 : 2^n - 1 = 원판이 이동하는 총 횟수. 그러므로 시간 복잡도는 O(x^n)이므로 최악.


# Disk movement baekjoon 1914, 11729
def hanoi_tower_move(N, start, end, middle): 
    if N == 1:
        print(start, end)
    else:
        # recursion : n-1 disks move to 2nd pole
        hanoi_tower_move(N-1, start, middle, end)   # 이거 실행하면 재귀로써 print(start, end)가 연쇄적으로 호출된다
        # move the biggest one to 3rd_pole
        print(start, end)
        # move n-1 disks in 2nd_pole to 3rd_pole
        hanoi_tower_move(N-1, middle, end, start)   # 이거 실행하면 재귀로써 print(start, end)가 연쇄적으로 호출된다


# # Disk movement baekjoon 1914, 11729
# def hanoi_tower_move(N, _1st, _3rd, _2nd): 
#     if N == 1:
#         print(_1st, _3rd)
#     else:
#         # recursion : n-1 disks move to 2nd pole
#         hanoi_tower_move(N-1, _1st, _2nd, _3rd) 
#         # move the biggest one to 3rd_pole
#         print(_1st, _3rd)
#         # move n-1 disks in 2nd_pole to 3rd_pole
#         hanoi_tower_move(N-1, _2nd, _3rd, _1st) 


# only for 11729
N= int(input())
print(hanoi_tower(N))
hanoi_tower_move(N, 1, 3, 2)

# # only for 1914
# N= int(input())
# if N > 20:
#     print(hanoi_tower(N))
# else:
#     print(hanoi_tower(N))
#     hanoi_tower_move(N, 1, 3, 2)
