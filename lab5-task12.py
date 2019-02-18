
class IP():
	def __init__(self,mylist,mask):
		self.list=mylist
		self.mask=mask

	def __str__(self):
		return f"IPv4 Address: [{self.list[0]}.{self.list[1]}.{self.list[2]}.{self.list[3]}/{self.mask}]"

	def getlist(self):
		newlist=self.list
		return newlist

	def getnetwork(self):
		return f"[{self.list[0]}.{self.list[1]}.{self.list[2]}.{self.list[3]}]"

	def convert(self,num):
                x=num%8
                line=x*'1'+(8-x)*'0'
                y=int(line, 2)
                return y

	def getmask(self):
		masklist=[255,255,255,255]
		if 0 < self.mask <8:
			masklist[0]=self.convert(self.mask)
			return [masklist[0],0,0,0]
		elif self.mask==8:
			return [255,0,0,0]
		elif 8 < self.mask < 16:
			masklist[1]=self.convert(self.mask)
			return [masklist[0],masklist[1],0,0]
		elif self.mask==16:
			return [255,255,0,0]
		elif 16 < self.mask < 24:
			masklist[2]=self.convert(self.mask)
			return [masklist[0],masklist[1],masklist[2],0]
		elif self.mask==24:
			return [255,255,255,0]
		else:
			masklist[3]=self.convert(self.mask)
			return [masklist[0],masklist[1],masklist[2],masklist[3]]



class Subnet(IP):
	"""Inherits from IP"""

	def __init__(self,mylist,mask):
		super().__init__(mylist,mask)


	def network(self):
		iplist=self.getlist()
		submask=self.getmask()
		address=[]
		for i in range(4):
			addr=iplist[i] & submask[i]
			address.append(addr)
		return f"Net Address: [{address[0]}.{address[1]}.{address[2]}.{address[3]}/{self.mask}]"

	def broadcast(self):
                iplist=self.getlist()
                submask=self.getmask()
                cast=[(255-submask[0]),(255-submask[1]),(255-submask[2]),(255-submask[3])]
                address=[]
                for i in range(4):
                        addr=iplist[i]|cast[i]
                        address.append(addr)
                return f"Broadcast Address: [{address[0]}.{address[1]}.{address[2]}.{address[3]}]"

	def hosts(self):
		number=pow(2,(32-self.mask))-2
		return f"No. of hosts in the network: {number}"

	def propmask(self):
		masklist=self.getmask()
		return f"Net Mask : [{masklist[0]}.{masklist[1]}.{masklist[2]}.{masklist[3]}"

Sub=Subnet([192,168,10,1],26)
print(Sub)
print(Sub.propmask())
print(Sub.network())
print(Sub.broadcast())
print(Sub.hosts())

