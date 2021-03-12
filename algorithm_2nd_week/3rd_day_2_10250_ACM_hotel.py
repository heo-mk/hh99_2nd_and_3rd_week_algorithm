import math
cnt = int(input())

for i in range(cnt):
    # h, w, n = input().split()
    # H, W, N = int(h), int(w), int(n)
    H, W, N = map(int, input().split())

    # digits for right
    num_right_room = math.ceil(N/H)
    print(num_right_room)
    
    if num_right_room > 0 and num_right_room < 10:
        two_digit_num_right_room = "0" + str(num_right_room)
    else:
        two_digit_num_right_room = str(num_right_room)     
    print(two_digit_num_right_room)
    
    # digits for left
    if N % H == 0:
        num_left_room = H
    else:
        num_left_room = N % H
    print(num_left_room)

    str_room_num = str(num_left_room) + two_digit_num_right_room
    room_num = int(str_room_num)
    print(room_num)