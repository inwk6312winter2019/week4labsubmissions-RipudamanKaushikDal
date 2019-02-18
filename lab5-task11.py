class IP():
	def __init__(self,mylist=[192,168,10,1],mask=26):
		self.list=mylist
		self.mask=mask

	def __str__(self):
		return f"[{self.list[0]}.{self.list[1]}.{self.list[2]}.{self.list[3]}/{self.mask}]"

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
			masklist[0]=ip.convert(self.mask)
			return f"[{masklist[0]}.0.0.0]"
		elif self.mask==8:
			return f"[255.0.0.0]"
		elif 8 < self.mask < 16:
			masklist[1]=ip.convert(self.mask)
			return f"[{masklist[0]}.{masklist[1]}.0.0]"
		elif self.mask==16:
			return f"[255.255.0.0]"
		elif 16 < self.mask < 24:
			masklist[2]=ip.convert(self.mask)
			return f"[{masklist[0]}.{masklist[1]}.{masklist[2]}.0]"
		elif self.mask==24:
			return f"[255.255.255.0]"
		else:
			masklist[3]=ip.convert(self.mask)
			return f"[{masklist[0]}.{masklist[1]}.{masklist[2]}.{masklist[3]}]"

ip=IP()
print('ipv4:',ip)
print('net:',ip.getnetwork())
print('mask:',ip.getmask())
