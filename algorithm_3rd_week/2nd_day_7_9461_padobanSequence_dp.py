# 백준 9461번 파도반 수열
import sys
input = sys.stdin.readline

padoban = {1:1, 2:1, 3:1}    # memoization을 위한 dict
# padoba 수열의 항 구하는 함수
# P(N) = P(N-3) + P(N-2)
def padoban_seq(n, padoban_memo):
    if n in padoban_memo:
        return padoban_memo[n]

    # memoization 하기
    nth_padoban = padoban_seq(n-3, padoban_memo) + padoban_seq(n-2, padoban_memo)
    padoban_memo[n] = nth_padoban
    return nth_padoban

T = int(input())   # test case 횟수
for i in range(T):
    inp = int(input())
    print(padoban_seq(inp, padoban))
    
# print(padoban_seq(int(input()), padoban))
# print(padoban_seq(int(input()), padoban))