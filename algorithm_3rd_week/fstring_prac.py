s1 = 'left'
s2 = 'mid'
s3 = 'right'

result1 = f'|{s1:<10}|'
result2 = f'|{s2:^10}|'
result3 = f'|{s3:>10}|'

print(result1)
print(result2)
print(result3)
print()

###
num = 10
result = f'my age {{{num}}}, {{num}}'
print(result)
print()

###
d = {'name':'BlockDMask', 'gender':'man', 'age':100}
result4 = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result4)
print()

n = [100, 200, 300]
print(f'list : {n[0]}, {n[1]}, {n[2]}')
print()
for v in n:
	print(f'list with for : {v}')
