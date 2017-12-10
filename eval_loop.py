def evaluate():
	a=''
	while(True):
		a= raw_input('Enter values or press q to quit\t')
		if(a=="q"):
			print 'Byeeeeeee'
			return 0
		print eval(a)

evaluate()