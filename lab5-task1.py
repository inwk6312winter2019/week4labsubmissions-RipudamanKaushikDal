
class Point():
    """Represents a point in 2-D space"""

blank=Point()
blank.p1=(5,6)
blank.p2=(9,10)

from math import sqrt
def dist_between_points(P1,P2):
	d=sqrt((P2[0]-P1[0])**2+(P2[1]-P1[1])**2)
	print(float(d))
dist_between_points(blank.p1,blank.p2)
