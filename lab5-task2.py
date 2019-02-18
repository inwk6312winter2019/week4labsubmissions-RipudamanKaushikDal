class Point():
	p1=(10,10)
P=Point()

class rectangle():
	width=200
	height=100
	corner=P.p1
rec=rectangle()

def find_center(box):
	x=(rec.corner[0]+rec.width)/2
	y=(rec.corner[1]+rec.height)/2
	print('The center is at:',(x,y))
find_center(rec)
