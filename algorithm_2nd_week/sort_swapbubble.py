input = [4, 6, 2, 9, 1]

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array) - 1 - i ):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            # print(j)
    return array

print(bubble_sort(input))

# array = [4, 6, 2, 9, 1]

# for i in range(len(array)-1):
#         for j in range(len(array) - 1 - i ):
#             print(j)