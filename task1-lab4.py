from string import *
def rem_pun(sent,new=""):
	for alpha in sent:
		for mark in punctuation:
			alpha=alpha.strip(mark)
		new+=alpha
	return new

def collect():
	fin=open("book.txt")
	line=fin.readlines()
	for words in line:
		noline=words.replace(" ","")
		for word in noline.split():
			nospace=word.strip(whitespace)
			p=rem_pun(nospace)
		print(p)
collect()
