class Point():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return f'({self.x},{self.y})'

	def __add__(self,other):
		sum=(self.x+other.x,self.y+other.y)
		return sum

p1=Point(3,4)
p2=Point(5,6)
print(p1)
print(p2)
print(p1+p2)
