def remove_duplicate():
	lists=[]
	new_list=[]
	lists=raw_input('enter text\t')
	for i in lists:
		if i in new_list:		
			continue	
		
		new_list.append(i)	

	
	print new_list	

remove_duplicate()