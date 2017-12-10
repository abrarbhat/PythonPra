import math

def check(a,b,c,n):

	power_of_abn = math.pow(a,n)+math.pow(b,n)
	power_of_c = math.pow(c,n)
	if power_of_abn == power_of_c:
		return "Fermut was right"
	else:
		return "Hahaaa"




print check(2,3,5,3)
