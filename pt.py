class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def assign(self,x,z):
		self.x=x
		self.y=y
	def print_line(self):
		print "X=%d and Y=%d"%(self.x,self.y)
	def __str__(self):
			return "X=%d and Y=%d"%(self.x,self.y)

	
pt= Point(10,20)
pt.print_line()
print pt
