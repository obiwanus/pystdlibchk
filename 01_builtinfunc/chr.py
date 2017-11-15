
for num in range(0, 0x10FFFF):
	try:
		print(chr(num), end='')
	except ValueError:
		print('-', end='')

