def del_list():
	listss= ['12','1asd2','1asds2','1a2','9','k']
	new_list=[]
	for i in listss:
		if i[0] !=[] or i[-1]!=[]:
			print "1",i
			continue
			print "2",i
	new_list.append(i)

	print 'old list ::',listss
	print 'new list ::',new_list
	print listss[-1]

del_list()	
