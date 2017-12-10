def uses_only(word,available):
	flag =0
	for letter in word:
		if(letter not in available):
			flag =1
			break

	if flag==1:
		print "More letters used"

	else:
		print "Only letters used"			

uses_only("abrar","rba")		