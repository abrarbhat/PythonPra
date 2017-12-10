def fact(n):
	space = ' '*(4*n)
	print space,'factorial',n
	if(n==0):
		print space,'returning',n
		return 1
	else:
		rec = fact(n-1)
		res = n* rec
		print space,'returning',n
		return res

print(fact(6))