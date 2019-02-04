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

def invert_dict(d):
        inverse = dict()
        for key in d:
                val=d[key]
                if val in inverse:
                        inverse[val].append(key)
                t=inverse.setdefault(val, [key])
                inverse[val]=t 
        mylist=list(inverse.items())
        mylist.sort(reverse=True)
        for i in range(20) :
            print(mylist[i])
invert_dict(hist())		
