num_class = int(input())
for i in range(num_class):
    class_grade = list(map(int, input().split(' ')))
    avg = sum(class_grade[1:])/class_grade[0]
    count = 0
    
    for score in class_grade[1:]:
        if score > avg:
            count += 1

    ratio_over_avg = (count/(len(class_grade)-1))*100 
    print(str('%.3f' %ratio_over_avg) + "%")


# for i in range(int(input())):
#     list_input = list(map(int, input().split(' ')))
#     ave = sum(list_input[1:]) / list_input[0]
#     count = 0
#     for j in list_input[1:]:
#         if j > ave:
#             count += 1
#     print(str('%.3f' % round(count / list_input[0] * 100, 3)) + '%')


