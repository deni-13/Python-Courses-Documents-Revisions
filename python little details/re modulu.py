import re
#regex kisa ozet------<
x="merhaba"


y=re.findall("merhaba",x)
yu=re.split("a", x)
r=re.sub("a","u",x)
g=re.search("merhaba",x )
i=re.findall("[a-z]",x)
b=re.findall("[^h-z]",x)
p=re.findall("^h",x) #aradigim ilk harf h mi??
j=re.findall("a$",x)
t=re.findall("\s",x) #bosluk ariyoruz
print(y)
print(yu)
print(r)

print(g.span()) 
# obje uzerinden kacınci karakterde baslar ve biter

print(g.end()) #nerde bitti?
print(i)
print(b) # h ve z  arasini disla
print(b)
print(j) #aradigim son karakter a mi?
print(t)



