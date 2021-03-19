T = int(input())


for _ in range(T):
    x,y = map(int,input().split())
    start = 0;end = y-x
    start_cnt =0;end_cnt = 0
    
    k = 1
    while start<end: #넘어갈때까지
        start +=k  
        start_cnt+=1
        if start >= end: #만약 같거나 넘어갈 경우
            break
        end -=k    
        end_cnt+=1 
        k+=1
    print(start_cnt+end_cnt)