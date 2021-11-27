#karakter dizileri uzerinde islemler

import re

#print(dir(re))

#match metodu

a="istanbul izmir turkey izmir"
#x=re.match("istanbul",a)
# print(x)
# print(dir(x))

# print(x.span()) #0-8
# print(x.group()) #nesneyi direk basti

#2.kisim
x=re.match("turkey",a) #none dondurdu  nasil bakicaz?
y=re.search("turkey",a)
print(x)
print(y)
print(y.span())
print(y.group()) #kendisi 
#butun eslesme listeleri
c=re.findall("izmir",a)
print(c)


#3.kisim metakarakter

c="newyork los angeles mexico amsterdam newyerk"
v=re.findall("newy[eo]rk",c) #o veya e olabilir aradaki harf
print(v)


f=["ahmet","mehmet","met","amet"]

for a in f:
    ne=re.search("[a-z]met",a)
    if ne:
        print(ne.group())

#araliklari kontrol edip arama yaptik






