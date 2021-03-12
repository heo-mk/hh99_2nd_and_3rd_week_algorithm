N, M = map(int, input().split()) # N = total number of trees, M = Target total lenght of trees
trees_length = list(map(int, input().split()))
max_tree = max(trees_length)

cut_heigth = []
for i in range(1, max_tree):
    cut_heigth.append(i)

total_cut_lengths = []
for j in cut_heigth:
    cut_tot_len = 0
    for k in trees_length:
        # total_cut_length = 0
        j_cut = [j]
        if k >= j:
            cut_tot_len += (k - j)
            # print(total_cut_length)   
        else:
            cut_tot_len += 0
    j_cut.append(cut_tot_len)
        # print(cut_len)		
    total_cut_lengths.append(j_cut)

# print(lengths)
print(total_cut_lengths)

def is_target_length(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if M == array[current_guess][1]:
            return array[current_guess][0]
        elif M < array[current_guess][1]:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max)//2
    
    return array[current_guess][0]

print(is_target_length(M, total_cut_lengths))