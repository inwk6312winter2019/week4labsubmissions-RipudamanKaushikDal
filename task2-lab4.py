fin=open('book.txt')
d=dict()
def hist():
	#d=dict()
	for line in fin:
		word=line.strip()
		for c in word.split():
			if c not in  d:

				d[c]=1
			else:
				d[c]+=1
	return d
print(hist())
print("No. of Words:",len(hist()))



	
	
