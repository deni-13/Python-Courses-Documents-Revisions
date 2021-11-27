import property1


x=property1.Bilgi("emre","ali")

print(x.ad,x.soyad)


#propert1py ad soyad yerine isim ve soyisim kullanalim...
#yani kaynak kismi degisssin! bu program calismicak 


#x.ad="ali" dersek calismicak
#cunku ilk programda degistirilemez bunu degistirmek icin setter kullanicaz.


x.ad="ali"
print(x.ad)
  
#burdaki ismi degistirmek istiyorsak

del x.ad

print(x.ad) #sildik bu sekilde bu programi baskalarnin 