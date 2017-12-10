import math
def rsa(msg):
	pn=7.0
	qn=17.0
	nn = pn*qn
	t_of_n =(pn-1)(qn-1)
	ee=17
	dd=2753
	cc=math.power(msg,ee)%nn
	print cc

	mm=math.power(cc,dd)%nn	

	print mm

rsa("alksdlk")	