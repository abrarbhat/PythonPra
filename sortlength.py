def sort_by_length(words):
	t=[]
	for word in words:
		t.append((len(word),word))
	t.sort(reverse=True)
	print t
	res=[]
	for length,word in t:
		res.append(word)
	print res	



words=raw_input()
sort_by_length(words)	