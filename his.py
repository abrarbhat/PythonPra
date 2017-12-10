def histogram():
	t=[]
	z=''
	d=dict()
	while True:
		z=raw_input('enter \t')
		if z=='d':
			break
		else:	
			t.append(z)
	length = len(t)-1
	count =0
	for i in d:
		if i not in t:
			t[count]=1
		else:
			t[count]+=1

	print t	

			

histogram()	
