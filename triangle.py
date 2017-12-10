def is_triangle():
	a=raw_input('value of a\t')
	b=raw_input('value of b\t')
	c=raw_input('value of c\t')

	if((a+b<c)or(a+c<b)or(b+c<a)):
		print "triangle cannot be formed"
	else:
		print "triangle can be formed"

is_triangle()
