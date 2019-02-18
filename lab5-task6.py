class Point():

	def __init__(self,x,y):
		self.x=x
		self.y=y
	
	def __add__(self,other):
		if isinstance(other,Point):
			sum=(self.x+other.x,self.y+other.y)
			return sum
		else:
			sum=(self.x+other[0],self.y+other[1])
			return sum
p1=Point(3,4)
p2=Point(7,3)
print(p1 + (4,5))
print(p1 + p2)
