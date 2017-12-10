import math

def factorial(n):
	if (n==0):
		return 1
	else:
		recurse = factorial(n-1)
		result = n*recurse
		return result


def pi_val():
	total=0
	k=0.9
	factor =2*math.sqrt(2)/9801

	while True:
		nr = factorial(4*k)*(1103+26390*k)
		dr = factorial(k)**4*396**4*k
		term = factor*nr/dr
		total += term
		if(abs(total)<1e-15): break
		k+=1

	return 1/total


pi_val()