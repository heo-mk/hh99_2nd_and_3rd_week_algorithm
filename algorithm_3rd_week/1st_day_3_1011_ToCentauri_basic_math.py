import sys
input = sys.stdin.readline
T = int(input())   # test case 횟수

# 금교석님의 방식. 
# 양끝에서 동시에 출발, 서로 만나거나 겹칠 때까지 동작. 
# 그때까지 양쪽에서부터 각각 이동한 횟수를 더한다. 
for i in range(T):
    x, y = map(int, input().split())
    start = 0; end = y-x           # 시작점과 끝점의 위치. 위치가 변하면서 갱신된다
    start_cnt = 0; end_cnt = 0   # 시작점과 끝점에서 이동하는 횟수

    k = 1   # 첫 이동거리
    while start < end:
        # 시작점과 끝점에서부터 이동하는 동작
        start += k
        start_cnt += 1
        # 시작점에서 이동한 것이 끝점에서 이동한 것과 
        # 만나거나 넘어갈 때까지 동작을 시행한다.
        if start >= end:    # if문이 여기 있어야 하는 이유는
            break           # 거리차가 1인 경우는 바로 끝내버리기 위해서다.
                            # if 문이 끝점 이동 동작 다음에 오면 거리차가 1이면 이동 동작이 겹쳐서 답이 2가 된다.
        end -= k
        end_cnt += 1
        
        if start >= end:
            break
        
        k += 1        # 다음번에는 이동폭이 1만큼 늘어난다. ex) 1 -> 2 -> 3 ... 이렇게 해야 최소 횟수로 이동한다. 
    print(start_cnt + end_cnt)
    
    
# 조상균님의 방식
T = int(input())   # test case 횟수
cases = []
for i in range(T):
    cases.append(list(map(int, input().split())))
    
result = []   # 결과 저장, 갱신 리스트
for case in cases:
    distance = case[1] - case[0]  # 이동 거리
    count = 0   # 이동횟수
    if distance == 0:
        count = 0
    elif distance == 1: 
        count = 1     # if, elif까지는 특수 경우. 거리가 0 or 1 일때
    else:
        num = 1       # 한번에 이동하는 거리. 1 -> 2 -> 3 식으로 증가 가능
        re = 0
        compare = 0   # 누적 이동 거리
        while compare < distance:
            if re == 0:
                re = 1 
                compare += num
            else:
                re = 0
                compare += num
                num += 1 
            count += 1
    result.append(count)
    
for st in result:
    print(st)