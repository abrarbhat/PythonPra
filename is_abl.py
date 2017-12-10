def isabl(str,lett):
	flag=0
	i=0
	length= len(str)-1
	while length>=0:
		if(lett[0]==str[i]):
			break
		i=i+1
		length= length-1
	
	if(str.substring(i)==lett):
		print "elements are in order"
	else:
		print "elements are not in order"


isabl("abrar","rar")

