import re


equation = '2+6/3-5/(5*2)+(1+1)/(3*3)'
valid = re.match('^[0-9*+-/()]+$', equation)

if valid:
	try:
		print(eval(equation))
	except Exception:
		pass
else:
	print('Invalid equation.')
