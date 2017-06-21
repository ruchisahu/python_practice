d=dict()
d['temp_india']=40
d['temp_usa']=7
for k,v in d.items():
    print(k,v)

#item()in dict returns list of (key-value ) tuples

tup=d.items()
print(tup)

#Tuple are comparable if first is equal check for second

print((0,1,2)<(2,3,0))

dict={'a':10,'b':1,'c':4}
print(dict.items())
print(sorted(dict.items()))                 #key sorted order not value



#sorted by value order

c={'a':6,'u':9,'r':2}
tmp=list()                      #tmp is a list but all the things ina list is tuple
for k,v in c.items():
	tmp.append((v,k))          #new tuple
print(tmp)
l=sorted(tmp)
print(sorted(tmp))


