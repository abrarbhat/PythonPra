def suff():
	prefixes ='JKLMNOPQ'
	suffix = 'ack'
	for letter in prefixes:
		if(letter =='Q' or letter=='O'):
			letter=letter+'U'
	print letter+suffix

suff()	