f=open('romeo.txt')
counts=dict()
for line in f:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

l=list()
for k,v in counts.items():
	new=(v,k)
	l.append(new)
l=sorted(l,reverse=True)	

for v,k in l[:10]:
	print(k,v)
   

#shorter version(list comprension)

c={'a':10,'c':2,'r':1}
print(sorted([(v,k) for k,v in c.items()]))

