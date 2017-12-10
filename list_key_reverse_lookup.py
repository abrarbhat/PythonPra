def reverselook():
	lists=dict()
	element=''
	i=0
	while element!='d':
		element = raw_input('enter or press d::\t')
		lists[i]=element
		i=i+1
	
	ke=[]
	ke.append('a')
	print "list created"
	sear=raw_input('Enter element to be searched\t')
	for c in lists:
		print c
		if sear==c:
			print ke
			ke.append(c)
			print ke
	print ke		

reverselook()	