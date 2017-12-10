def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True
		else:
			return False

def any_lowercase2(s):
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'

def fl(s):
	#flag=False
	for c in s:
		flag = c.islower()
	return flag	 


print fl('a')

