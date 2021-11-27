#property kavrami

class Bilgi():
    def __init__(self,ad,soyad):
        self.isim=ad
        self.soyisim=soyad

        
    #property

    @property

    def ad(self):
        return self.isim
    #degiskeni degistirmek icin

    @ad.setter #decorator
    def ad(self,yeni):
        self.isim=yeni
    @ad.deleter
    def ad(self):
        self.isim=None

    @property
    def soyad(self):
        return self.soyisim

