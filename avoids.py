def avoid(word,letters):
	length=len(word)-1
	index=0
	flag=0
	while(length>=0):
		if(word[index] in letters):
			flag=1
			break
		index=index+1
		length=length-1
	if flag == 0:
		print "Not found"	
	else:
		print "Found"

avoid('abrar','ccccca')			