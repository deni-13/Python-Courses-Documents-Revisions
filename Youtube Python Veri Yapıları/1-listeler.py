#listeler--> array,linkedlist gibi---> 6 November 2021 23:27

l=[1,2,3,4]

print(l)
l.append(8) #metodlar

#aralara sokmak

l.insert(5,3) #5.sıraya 3ü ekle

l.remove(2)


# 2 elemanı cıkarcaz
#%%
# =============================================================================
# l=[1,2,45,78,4,723,8]
# print(l.pop()) #cikan elemanlari basicak
# #stack yapısında pop ve append kullanabiliyoruz
# 
# print(l.index(2)) #2 sayisinin nerde old buluyoruz
# 
# 
# 
# print(l.count(5)) #5 kac tane var???
# =============================================================================
 

l=[6,4,79,455,667,326,0,93,5]
l.sort()

print(l)

   #%%
test = [-2, -5, -1, -10, 0, -17]
test.sort(reverse=True)
print(test)


#extend

l2=[1,3,5,657,3]

l.extend(l2)

#listeyi listeyi ekleme

#eger append yapsaydık onu tek bir eleman gibi alirdi.


l.clear() #listeyi komple bosaltıyor

#copyalama


#shallow ve  deep kopyalama


#derin olanda - pointer
l3=l2

l3.append(600)
"""
tek varliga iki sekilde hafizada erisiliyor.

"""

#♠copy --> shallow

l5=l2.copy()

#hafızaada farkli yerde olmasi
#ilk kopyada bu sekilde etkilemiyor.
l5.append(67)

