def bisect(str):
	#str=raw_input('Enter Element')
	let=raw_input('Enter Element to be found')
	print let
	low=0
	high=len(str)
	mid=low+high/2
	flag=0
	length= len(str)
	while(length>=0):
		print mid
		length=length-1
		if(str[mid]==let):
			i=mid
			flag=1
			break
		elif(let>=str[mid]):	
			low=mid
			mid=(low+high)/2
		else:
			high=mid
			mid=(low+high)/2


	if(flag==0):
		print "not found"
	else:
		print "found at",i


str=['a','b','d','f','g']

bisect(str)			