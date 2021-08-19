#Tekrar-2

#kosullar

print(1>7)
print(10==12)
#genelde if else icinde

print(not False)

age=int(input("yas gir"))


if age>25 :
    print("kulube girebilirsin")
else:
    print("yasak")
    #%%
#ornek gelistirme

print("**********ATM*******")


db_ku="deniz"
db_parol="gd65"

kulla=input("Kullanıcı adı--->")
par=input("parola---->")

if kulla !=db_ku and  par != db_parol :
    print("hatali")

elif kulla == db_ku and  par != db_parol :
    print("parola hatali")
    
elif kulla !=db_ku and  par == db_parol :
    print("kullanıcı adi yanlis")
    
else:
    print("tebrikler")
    
#%% Ic ice kosul

x=10

if x>5:
    if x>6:
        print("a")
    
    
    
#%%exercise:
    
    
maas=int(input("Salary?"))


if maas<=1000:
    print(maas+maas*0.15)
elif maas<=2000:
    print(maas*0.1+maas)
elif maas<=3000:
    print(maas*0.05+maas)
elif maas>3000:
    print(maas*0.02+maas)
    
    
#%%loops
"""
for item in "Python":
    print(item)


"""
   
#range
for i in range(8,0,-1):
    print(i)
   
    
#ennumarate-->key ve value basmak

#while


a=0

while(a<10):
    a+=1
    print(a)
    
    
    
#%% exercise

email=["rgr.com","dvd4.com","aa56.com"]

dp=[]

for e in email:
    if email.count(e)>1 and e not in dp:
        dp.append(e)
        
print(dp)













   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    