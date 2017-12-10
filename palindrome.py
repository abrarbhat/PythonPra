def is_palindrome(a):
		
	length= len(a)-1
	b =""
	while(length >=0 ):
		#b.append(a[length])
		b=b+a[length]
		length=length-1
	
	if a==b:
		return "palindrome found"
	else:
		return "palindrome not found"

print(is_palindrome('io'))