x = 3
password = 'a123456'
while x > 0:
	code = input('type your password: ')
	if code == password:
		print('accessed')
		break
	else:
		x = x - 1
		if x == 0:
			break
		print('u still have', x, 'chance')

