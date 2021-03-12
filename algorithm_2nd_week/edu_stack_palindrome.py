def palindrom(s):
	qu = []
	st = []
	for x in s:
		if x.isalpha():
			qu.append(x.lower())
			st.append(x.lower())
	print(qu)
	print(st)

	while qu:
		if qu.pop(0) != st.pop():
			return False
	return True

print(palindrom("WoW"))
# print(palindrom("Madam, I'm Adam."))
# print(palindrom("Madam, I am Adam."))