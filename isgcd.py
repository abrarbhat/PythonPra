def is_gcd():

	a= int(raw_input('Enter value of a::\t'))
	b= int(raw_input('Enter value of b::\t'))

	remab = a%b


	remb = b%remab

	print "Greatest Common Divisor of A and B ::",remb

is_gcd()	