#%%fonksiyonlar


#repeating tasks

def blowf():
    print("fire")
    
blowf()


#arguments and parameters

def blowe(name,fire):
    print(f"{name} {fire}")
    
blowe("raelle","a")

#%%return

def multiplier(a,b):
    return a*b

multiplier(7,3)    
#ORNEKLER

def sum(a,b):
    value=a+b
    return value

j=sum(3,88)
print(j)

#%% positive neg 

def func(x):
    if x>0:
        return "positive"
    elif x<0:
        return "negative"
    else:
        return "0"
        
        
print(func(-10))


 #%%factorial


def fact(num):
    facto=1
    if num==0 or num==1:
        return 1
    else:
        while(num>1):
            facto=facto*num
            num-=1
            
    print(facto)
    
fact(3)    

#%%scope

num=1  #global fonk'da kullanilmaz

def conf():
    
    num=10
    return num
conf()

#lambda

a=(lambda x:x+1)(2)

print(a)

#methodlar
s=input("isim gir--->") 
print(s.upper())

#%%exceptions
"""
#bug example
n1=input("deger gir--->")
n2=input("deger gir--->")

print(n1+n2)
"""
#exception handling
a="apple"

try:
    print(int(a))
except TypeError:
    print("sayi gir!!!!")
    


 
 
       
        
        
        
        
        
        
        
        
        
        