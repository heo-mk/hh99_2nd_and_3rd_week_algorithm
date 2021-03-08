###################################
############ 내 풀이 ##############
###################################
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    string = string.upper()
    print(string)

    for char in string:
        if not char.isalpha():
            continue                                   # if의 조건이 참인 부분은 건너뛰고 다음 단계에서 진행
        arr_index = ord(char) - ord('A')
        # print(arr_index)
        alphabet_occurrence_array[arr_index] += 1      # 상대위치 relative position.
    
    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] > max_occurrence:
            max_occurrence = alphabet_occurrence_array[index]
            max_alphabet_index = index
            print(max_occurrence)
            print(max_alphabet_index)
            print()
    
    print(alphabet_occurrence_array)
    print(max_alphabet_index)

    max_value_in_array = max(alphabet_occurrence_array)
    print(max_value_in_array)
    max_value_in_array_cnt = alphabet_occurrence_array.count(max_value_in_array) 

    if max_value_in_array_cnt > 1:
        max_alphabet = "?"
    else:
        max_alphabet = chr(max_alphabet_index + ord('A')).upper()   

    return max_alphabet


print(find_alphabet_occurrence_array('This is sparta!'))
print()
print(find_alphabet_occurrence_array('Mississipi'))
print()
print(find_alphabet_occurrence_array('oOaaaaegl'))
print()
print(find_alphabet_occurrence_array('k'))


###################################
######## 백준 다른 답안 ###########
###################################

word = input().upper()
word_list = list(set(word))
print(word_list)
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)
    print(cnt)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])