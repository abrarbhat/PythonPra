known ={0:'a',1:'b'}
def exam():
	known[2]= 1
	print known
	global known
	known =dict()

exam()	