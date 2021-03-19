# 다이나믹 프로그래밍 = 기억하면서 풀기
# 재귀 함수를 기억하면서 풀기 함수로 바꿔 쓰기
from cyberbrain import trace
import sys
input = sys.stdin.readline
import time


# memoization을 위한 dict
# dict로 하면 원하는 값을 찾아서 새 값을 저장하는 과정에서 
# 시간 복잡도가 O(n)으로 효율이 좋다.
w_memo = {}

@trace
def w(a, b, c):
    # memonization
    # 이름이 key인 이유는 dict의 키로 입력할 값이라서.
    # key = str(str(a) + ',' + str(b) + ',' + str(c))
    key = f'{a},{b},{c}'  
    if key in w_memo:
        return w_memo[key]
    # 이렇게 되면 meme dict에는 키-값이 다음과 같이 저장된다.
    # {string:값, ...}
    # {'-1,-1,-1':key-1, '0,0,0':key0, '1,1,1':key1, ...}
    
    # w_memonization
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    # 위의 if문은 return 1으로 함수가 끝난다.
    # 여기서는 위의 if문과 별개의 if문으로 돌리는 과정이 들어간다.
    # 그래서 각 if문마다 return으로 함수를 끝낼게 아니라면
    # if, elif, elif ..., elif, else 의 순서로 간다.
    if a > 20 or b > 20 or c > 20:
        w_memo[key] = w(20, 20, 20)
    elif a < b and b < c:
        w_memo[key] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else: 
        w_memo[key] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return w_memo[key]  # 이번 if문의 종료 조건

@trace
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    result = w(a, b, c)
    # print(w_memo)
    print('w(a, b, ,c) = {}'.format(result))    