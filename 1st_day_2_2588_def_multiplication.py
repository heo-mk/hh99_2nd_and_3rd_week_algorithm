def triple_multiple(n1, n2):
    # ex) n1 = 347, n2 = 214
    n2 = str(n2)
    n2_3, n2_2, n2_1 = n2[0], n2[1], n2[2] 
    
    n2_3 = int(n2_3)   # n2_3 = 2
    n2_2 = int(n2_2)   # n2_2 = 1         
    n2_1 = int(n2_1)   # n2_1 = 4

    result_3 = n1 * n2_3   # 347 x 2   (5)
    result_2 = n1 * n2_2   # 347 x 1   (4)
    result_1 = n1 * n2_1   # 347 x 4   (3)

    multiple = 0
    multiple = result_3 * 100 + result_2 * 10 + result_1    # (6)
    
    return result_1, result_2, result_3, multiple

a = int(input())
b = int(input())

print(triple_multiple(a, b))
