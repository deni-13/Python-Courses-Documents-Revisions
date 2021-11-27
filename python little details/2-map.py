#listelerde kullanılır

#mapsiz

def kare(liste):
    liste3=[]

    for eleman in liste:
        liste3.append(eleman**2)
    return liste3
print(kare([2,4,6,4,43]))

#map'li daha kisa kullanim!!!


j=[1,2,3,6]

print(map(lambda x:x**3,j)) #bu hali bir adress veriyor!
print(list(map(lambda x:x**3,j)))


#ornek 2

a=[12,46,3,6]
b=[1,2,4,5,6]


print(list(map(lambda x,y:x+y,a,b)))