# https://github.com/VasilyDrozhzhin/Module_9/blob/main/Module_9_6.py
def  all_variants(text):
	length = len(text)
	for sub_length in range(1, length + 1):
		for start in range(length - sub_length + 1):
			end = start + sub_length
			yield text[start:end]


a = all_variants("abc")
for i in a:
	print(i)


