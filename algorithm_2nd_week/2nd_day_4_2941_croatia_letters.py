# croatia_string = input()
# num_croatia_letter = 0
# letter_cnt = len(croatia_string)

# for i in range(letter_cnt):
#     if croatia_string[i:i+2] == 'c=' or 'c-' or 'd-' or 'lj' or 'nj' or 's=' or 'z=':
#         num_croatia_letter += 1
#         letter_cnt -= num_croatia_letter
#         print(letter_cnt)
#         print()
#     elif croatia_string[i:i+3] == 'dz=':
#         num_croatia_letter += 1
#         letter_cnt -= num_croatia_letter
#         print(letter_cnt)

# print(letter_cnt)

croatia_letters = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
letters = input()
for i in croatia_letters:
    letters = letters.replace(i, 'a')

print(len(letters))
