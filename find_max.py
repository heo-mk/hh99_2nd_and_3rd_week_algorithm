input = [3, 5, 6, 1, 2, 4]


# def find_max_num(array):
#     # 이 부분을 채워보세요!
#     max = array[0]
#     for i in range(1, len(array)):
#         if max < array[i]:
#             max = array[i] 
#     return max


# print(result)

def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num

result = find_max_num(input)
print(result)