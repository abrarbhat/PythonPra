def is_reverse(w1,w2):
	if len(w1) != len(w2):
		print "length not equal"
		return False

	i=0
	j=len(w2)-1

while j>=0:
	if w1[i] != w2[j]:
		print "char not equal"
		return False
	i=i+1
	j=j-1
	print i,'\t',j
	return True


print is_reverse('madam','amdam')