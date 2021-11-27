#Daha kısa daha pratik

k=lambda x:x**4

print(k(2))


#ozellikle gui de baazı fonksiyonlarda oldukca pratik 

#2.ornek

bk=lambda x,y : x if x>y else y
print(bk(3,5))

#lamdasız

def buykuc(x,y):
    if x>y:
        return x
    
    else:
        return y

print(buykuc(3,4))
