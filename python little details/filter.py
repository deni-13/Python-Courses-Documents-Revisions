#dizi veya tuple'da filtreleme

def y(liste):
    yli=[a for a in liste if a%3==0]
    return yli

sa=[1,2,54,5666,9,0,5]
print(y(sa))


#Filter ile yapalim


sa=[1,2,54,5666,9,0,5]
print(list(filter(lambda x:x%3==0,sa)))
#Burada if kullanmadik direk filter kullandik!