M =[
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [2, 1, 0, 0, 3, 0, 1, 1],
    [2, 1, 0, 0, 3, 0, 1, 1],
    [2, 1, 0, 0, 3, 0, 1, 1],
    [2, 1, 0, 0, 3, 0, 1, 1],
]

def print2D(arr2D):
    for i in range(len(arr2D)):
        for j in range(len(arr2D[0])):
            print(arr2D[i][j],end = " ")
        print()
    print()
    
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

mid = len(M)//2
print2D(split_2D_array(M[mid:],"left"))
print2D(split_2D_array(M[mid:],"right"))