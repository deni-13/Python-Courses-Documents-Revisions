#temelll-1



"""
cmt -pzr calısmıyoruz
evden ise--> 1.5 tl
is-->ev -- 1.4 tl
masraf=(gunxgidis+donus )


"""
gidis=1.5
donus=1.4

gun=input(" hafta ici mi hafta sonu mu-->")
if gun=="hafta ici":
    a=int(input("kac gun?"))
    masraf=a*(gidis+donus)
    yıllık=12*4*5*(1.5+1.4)
    print(f"toplam--> {masraf} yıllık -->  {yıllık}")
    
else:
    print("masrafsizsin!!")


    
#%%
#daire alanı

pi=3.14

r=float(input("yaricap??"))

alan=pi*r**2

print(alan)
#%%
#input!!!

yas=int(input("kac yas??"))
print("yasın",yas)

#len fonk sadece strde calisir
a=23
print(str(a)+str(7))#•---> 237

#%%eval 

print("""************calculator
       
      +
      -
      /
      *    
       
 **************""")
veri=input("islem???")
 
hesap=eval(veri)
print(hesap)



#karakter dizilerini eval () isliyor
 

#sabit disk silebilme durumu var


#%%if else

yas=int(input("yas kac???"))

if yas>30:
    print("girebilirsiniz")
else:
    print("giremezsin")
#%%if else ornek program
print(     """***
      
ornek   parola programi
      
      ***""")
parola=input("parola gir harflerden olusan--->")
if len(parola) > 8:
    print("kaydedildi parola uzunlugu {}".format(len(parola)))
    print("Tebrikler!!!!")
else:
    print("daha uzun gir")


#%%loops
a=5
while a<10:
    print("uu")
    a+=1
    #for
    
harfler="abcdef"

for i in harfler:
    print(i)

#while version
harf=   "qwerty"
a=0
while a<len(harf):
    print(harf[a])
    a+=1
    
#ornekk

har="şçöüğ"
parola=input("enter the password:")

for i in har:
    if  i in  parola:
        print("no")




#%%eval !!!!!!!!

izinli="0123456789+-/*"


while True:
    veri=input("islem???")
    if veri=="q":
        break
    for s in veri:
        if s not in izinli:
            print("NO!!!!!")
            quit()
        hesap=eval(veri)
        print(hesap)            
#%%ilgi araclari
#♠break continue

for i in range(3):
    parola = input("parola belirleyin: ")
    if not parola:
        print("parola bölümü boş geçilemez!")

    elif len(parola) in range(3, 8):
        print("Yeni parolanız", parola)
        break

    elif i == 2:
        print("parolayı 3 kez yanlış girdiniz.",
        "Lütfen 30 dakika sonra tekrar deneyin!")

    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")


#%%
"""
 for i in range(10, 0, -3):
     print(i)
"""

while True:
    parola = input("parola belirleyin: ")

    if not parola:
	#print("parola bölümü boş geçilemez!")
        pass

    elif len(parola) in range(3, 8): #eğer parolanın uzunluğu 3 ile 8 karakter
        #aralığında ise...
        print("Yeni parolanız", parola)
        break

    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

#%% errors
"""
karekok=int(input("sayi gir--->"))
hesap=karekok**0.5

print(hesap)
#ya harf girersek??
"""
    
#try--> hata verilcek kod
#except hata adi
k=int(input("sayi gir--->"))
l=int(input("sayi gir--->"))


try:
    print(k/l)
except ZeroDivisionError:
    print("bolemezsin")
except ValueError:
    print("sayi gir!!!!!!")
    
#%%lists

a=[1,2,3,445,78,0]
print(a[-1])


a="istanbulgalatasaray"
lis=a.split()
print(lis)
"""
a=list() 
a=[]   hepsi ayni
a=""
"""

#list
print(list(range(0,50))) #0 dan 50ye kadar


#methodlar baska sayfada...




#%% files


f=open("met.txt","w")
f.write("hesaplamaaaaaa")
f.close()

#read,readline,readlines

f=open("met.txt","r")
print(f.readline())


f=open("met.txt","r")
print(f.readlines())
#listeye atama readlines

f.close()


#degisiklik yapma

with open("data.txt","a")as f:
    f.write("sssssss")
    
#ekleme

with open("data.txt","r+")as f:
    veri=f.read()
    f.seek(0)
    f.write("ooooooooo"+veri)
    #onune ekledi
    #hem okuma hem yazma
    


#%% fonksiyonlar

"""
def s(isim,iss):
    print ("merhaba" ,isim,iss)
    
    
s("deniz","muhendis")

"""



#recursive fonksiyonlar
def fact(sayi):
    i=1
    while sayi>=1:
        i=sayi*i
        sayi-=1
    print(i)

fact(4)


def fak(sayi):
    if sayi==1:
        return 1
    else:
        return sayi *fak(sayi-1)
         
print(fak(5))


#fibonacci

def fib(a):
    if a<=2:
        return 1
    
    else:
        return fib(a-1)+fib(a-2)


print(fib(4))    





















