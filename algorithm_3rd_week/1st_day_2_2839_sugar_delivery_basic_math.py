# # 설탕 배달 봉지 최소화, 최소 갯수 맞추기
# # 몫(//), 나머지(%) 이용
# # 봉지 규격은 3kg, 5kg
# # 5kg 봉지를 많이 쓸수록 봉지수 줄인다

# # 입력하는 설탕량
# N = int(input())

# # 5kg 봉지가 많을수록 좋으므로 5로 나눈 나머지를 조건에 맞게 구분한다.
# def min_bags(n):
#     # 아래 숫자를 제외하면 모두 5의 배수 + 3의 배수 모양이 된다.
#     # if n == 4 or n == 7:
#     #     return -1
    
#     # 5kg 봉지수, 3kg 봉지수의 초기 리스트
#     bags = {5:0, 3:0}
#     min_num = []
#     quotient = n // 5
#     print(quotient)
#     for five_bag in range(quotient+1):
#         # 5의 배수에서 원래수 n을 빼고 남은 값.
#         print(five_bag)
#         three_remainder = (n - (five_bag * 5))
#         print(three_remainder)
#         # 이걸 3으로 나눈 나머지가 0 이라면, 3으로 나눈 몫이 3kg 봉지 갯수. 
#         if three_remainder % 3 == 0:
#             bags[5] = five_bag
#             bags[3] = (three_remainder // 3)
#             min_num.append(bags[5] + bags[3])
#             # 리스트 min_nums의 원소중 가장 작은 값이 최소 봉지 갯수
        
#         print(min_num)
#         print(bags)
        
#     result = min(min_num)
    
#     return result

# print()
# print(min_bags(N))


########## 금교석님 풀이 ################
# 5의 배수인가 -> 아니라면 3을 빼고 5의 배수인지 체크.
N = int(input())

count = 0
while N > 0:
    if N % 5 == 0:       # 먼저 5의 배수인가 검사
        count += N//5    
        break
    else:
        N -= 3           # 5의 배수가 아니라면 3을 뺀다. 
        count += 1       # 이 과정을 거듭해서 N % 5 == 0이 되면 N = 5x + 3y 이 성립한다. 그리고 출력값 = x + y

if N < 0:
    print(-1)     
else:             # N == 0인 상황이다.
    print(count)  # 3, 6, 9 같은 10보다 작은 3의 배수가 이에 해당.