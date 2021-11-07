#liste insaa
l=[]

for x in range(1,10):
    l.append(x**2)
    
    
print(l)
print(x) #dongu dısında baska bi yerde x bu bir yan etki! 

#side effect!!!

#amac disinda kullanilmasi

#%%functional programming
square=list(map(lambda x:x**2,range(1,11)))
print(square)


def f(x):
    return x+5
l2=[2,4,5,6]

print(list(map(f,l2)))


#f fonksiyonunu l2 ye uygula map ile bunu gerceklestrirdik! 
#listeye cevirmezsek bunu map object olarak basar!


print(list(map(lambda x:x+5,l2)))

#inline statement olarak lambda


#%%list comprehension


l3= [x**3 for x in range(10)]

print(l3)
print(x) #xin son degeri olan yan etki


#xler icin uygula



#%% lambda calculus for list comprehension 

l4=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y ]



#3x3=9 dongu ve her biri icin bir liste oluscak






