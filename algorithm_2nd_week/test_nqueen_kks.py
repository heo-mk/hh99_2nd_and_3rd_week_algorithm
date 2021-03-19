cnt = 0
col_set = set()
r_diagonal_set =set()
l_diagonal_set =set()

def NQueen(row,col):

    # 종료조건 branch 하는 곳
    global cnt
    if col in col_set:
        return
    
    r_diagonal = row-col
    l_diagonal = row+col
    
    
    if r_diagonal in r_diagonal_set:
        return
    if l_diagonal in l_diagonal_set:
        return
    
    # 정답조건 밑에 까지 다왔다는 뜻이므로
    if row==N-1:
        cnt+=1
        return
    
    col_set.add(col)
    r_diagonal_set.add(r_diagonal)
    l_diagonal_set.add(l_diagonal)
    # 후보선택
    for i in range(N):
        if i!=col:
            NQueen(row+1,i)
    
    # 아니라면 다시 backtracking 하면서 원래대로 복구하기
    col_set.remove(col)
    r_diagonal_set.remove(r_diagonal)
    l_diagonal_set.remove(l_diagonal)

N = int(input())
for i in range(N):
    NQueen(0,i)
print(cnt)
    
    
    
    