import sys
input = sys.stdin.readline

formula = input().split('-')  # formula는 '-' 를 단위로 잘린 문자열들이 모인 리스트
# ex : 5 + 30 + 90 - 80 + 20 - 100 + 60 -> ['5 + 30 + 90 ', ' 80 + 20 ', ' 100 + 60\n']
_1st_sum = 0

# 첫 '-' 전에 나온 숫자들의 합 
for i in formula[0].split('+'):   # '5 + 30 + 90 '
    _1st_sum += int(i)

# 첫 '-' 다음에 나오는 모든 수들의 합(부호와 상관없음)
_remain_sum = 0
for j in formula[1:]:  # ' 80 + 20 ', ' 100 + 60\n']
    for k in j.split('+'):  # ex : j = ' 80 + 20 '
        _remain_sum += int(k)

min_result = _1st_sum - _remain_sum
print(min_result)



# for i in range(len(formula)):
    # formula[i] == int(formula[i]) : 이려면 틀림 

# 이렇게 문자열로 둔 상태로 수정하는 건 잘 안 됨.
# formula = input().split('-')
# print(formula)
# print(type(formula))

# for i in range(len(formula)):
#     if i == '-':
#         for j in range(i+1, len(formula)):
#             if j == '+':
#                 j = '-'
#             print(formula)
                

# print(formula)
# print(type(formula))