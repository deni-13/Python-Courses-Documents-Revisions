#lists of list---> matrixes


l=[1,2,3]

m=[[4,2,3],[4,6,23],l]


k=[[[1,2,3],[2,3,4]],[[1,2,3],[1,24,9]],[[1,1]]] #bole farkli boyutta olbilrler

#%%m icin transpoze islemi

mt=[[row[i] for row in m ] for i in range(3)]

print(mt)

print(len(mt))


# del eleman silmeye yariyor

del(k[1])




 #%% tuples --> immutable
f=(1,2,43,5)
print(f)

#liste tutulabilir icinde ve bý listeyi maniple ettik.
h=([1,3,5],[3,9,3])

h[1][0]=1000

print(h)


#%%sets

y={1,3,5}


#stringi sete

e=set("hellopython")
j=set("kara")


#union operatoru

print(e|j)

#difference
print(e-j)

#intersect

print(e&j) #bos kume!



#%% dictionaries

tel={"jack":456,"jon":789}


#looping


for keys,values in tel.items():
    print(keys)
    print(values)





