#aleni/gizli-yarıgizli sinif uyeleri

class East():
    __kisiler_=[]  #gizli uye--> disaridan fonk cagrirsak ayni sekilde eleman 2 defa cikiyor bunun 
    #onune gecmek icin __ _
    
    

    def __init__(self,isim):
        self.isim=isim
        self.ekle()
    def ekle(self):
        self.__kisiler_.append(self.isim)
        print(self.isim,"listeye eklendi")

aa=East("emre")
    
#print(dir(East))--> burda kisiler de cikti


print(aa._East__kisiler_) #ulasabilmek icin
#ama aa.__kisiler_ yazarsak ulasamiyoruz!!!

#onune 1 underscore koyarsak yari gizli oluyor!!
