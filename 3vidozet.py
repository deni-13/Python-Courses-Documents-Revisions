#%%if else


x=int(input("bir sayi gir"))

if x<50:
    print("kucuk")
elif x>50:
    print("buyuk")
else:
    print("esit")
    

#%%for 
top=0
l1=[1,2,3,4]


for i in l1:
    top=top+i
    print(i)
print(top)
#range kullanimi
a=range(1,40,3)

print(a)
#%% ornek program --->tek olanlar
for c in  range(1,20):
    if c%2==0:
        continue
    print(c)
    #elsesiz  kullanim
    
    

#%%fonksiyonlar
#cift mi?
def f(sayi):
    if sayi%2==0:
        return True
    else:
        return False
    
print(f(45))



def g(s):
    
    print("merhaba"+" "+str(s))
    
    
g("python")



#factoriel

def fact(n):
    a=1
    sonuc=1
    while a<n:
        sonuc=sonuc*a
        a=a+1
    return sonuc
print(fact(5))
        
     
        #recursive yazim:
    #  #factoriyel  
def facto(n):
    if n==1:
        return 1
    return facto(n-1)*n

print(facto(5))    


#fibonacci


def fib(a):
    
    if a==0: return 0
    if a==1: return 1
    
    return fib(a-1)+fib(a-2)


print(fib(7))


