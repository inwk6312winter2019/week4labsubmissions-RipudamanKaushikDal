class Kangaroo():
	def __init__(self,pouch_contents=None):
		if pouch_contents==None:
			pouch_contents=[]
		self.pouch_contents=pouch_contents
	def put_in_pouch(self,other):
		self.pouch_contents.append(other)
	def __str__(self):
		return f'The pouch contains {self.pouch_contents}'
kanga=Kangaroo()
roo=Kangaroo()
kanga.put_in_pouch('ready')
kanga.put_in_pouch('go')

roo.put_in_pouch('123')
kanga.put_in_pouch(roo)

print(kanga)

print(kanga)
