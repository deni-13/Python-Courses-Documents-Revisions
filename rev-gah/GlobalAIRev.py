#Revision -1

#%% Veri Tipleri


num=20

num2=7.7 #float
print(type(num2)) #float

#matematiksel fonk

print(round(4.78))
print(abs(-765))
#print 
print("hello") #str 
a=34532
print(a)


#math op.

x=8
print(x/3)
print(x*3+2)

g=int(3.3)
print(g**2)

#%%String

name ="Java"
name1='C++'

a=type(name)
print(a)
print(name+" "+ name1)
b="7"
n="4"

#%%type conversion

a="john"

age=25

print(a+str(age))


first='john'
sec='smith'

print(f"hosgeldin {first} {sec}")

#%%Str indexing
#[start:stop::step over]

w="istanbul"

a=w[0:2]
print(a) #is
print(w[0::1]) #1er 1er say
print(w[::2]) #2ser
print(w[::3]) 
print(w[1::]) #1den basla sonuna kadar
print(w[::])
print(w[::-1]) #ters yazma

#%% logic op

iyi =True
kirli=False

print(True or False)
print(True and False)

#%%lists
fav=["ny","la","minesota"]

fav[0]="Texas"


clone =fav[::]
print(clone)


name="johnson"
k=name[::-1]
print(k)

#append,insert,extend

r=[34,24,2,7,22,3]

r.append(100)
print(r)

r.insert(5,4) #inserted value to 5th index
print(r)

r.extend([1,3,42,523,7674]) #other list extended
print(r)

#pop ,remove ,clear


#last element is deleted
r.pop()
print(r)

r.remove(2) #element is deleted
print(r)

r.clear()
print(r)  #empty list


y=["a","b","o"]

print[y.index("a")] 
#which index?


#count


t=y.count("a")
#adedi



rr=y.copy()
print(rr)
#copy

#%%
user={"name":"john",
      "age": 32,
      "married" :False}

print(user["name"])

print(user.values())

print("name"in user.keys())
#icindeki degerlr konrol ediyor









