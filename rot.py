def rotates():

	str = raw_input('Enter Value Of string ::\t')
	nums = int(raw_input('Enter Value Of Number ::\t'))
	length = len(str)-1
	arr = []
	i=0
	arr2 =[]
	while length >= 0:
		arr.append(ord(str[i])+nums)
		i=i+1
		length=length-1

	i=0
	length=len(arr)-1
		
	while length>=0:

		arr2.append(chr(arr[i]))
		i=i+1	
		length = length-1
	
	print (*arr)

rotates()