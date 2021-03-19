def split_2D_array(arr2D,direction):
    mid = len(arr2D[0])//2
    split_array =[]
    if direction=="left":
        for i in range(0,mid):
            split_array.append(arr2D[i][:mid])
    else:
        for i in range(0,mid):
            split_array.append(arr2D[i][mid:])
    return split_array
    

def is_same_color(arr2D):
    target = arr2D[0][0]
    for i in range(len(arr2D)):
        for j in range(len(arr2D[0])):
            if arr2D[i][j]!=target:
                return False
    return True


def find_blue_white(arr2D):
    # 끝내기 조건
    if is_same_color(arr2D):
        blue =0; white =0
        if arr2D[0][0]==1:
            blue+=1
        else:
            white+=1
        return (blue,white)
    
    #나누기
    colors =[0]*4
    mid = len(arr2D)//2
    colors[0]=find_blue_white(split_2D_array(arr2D[:mid],"left")) #첫번째
    colors[1]=find_blue_white(split_2D_array(arr2D[:mid],"right")) #두번째
    colors[2]=find_blue_white(split_2D_array(arr2D[mid:],"left")) #세번째
    colors[3]=find_blue_white(split_2D_array(arr2D[mid:],"right")) #네번째
    
    #더하기
    blue = 0;white=0
    for color in colors: 
        blue+=color[0]
        white+=color[1]
    
    return(blue,white)

N = int(input())
paper =[]
for _ in range(N):
    row=list(map(int,input().split()))
    paper.append(row)
    
blue,white = find_blue_white(paper)
print(white)
print(blue)