#asal programi

eleman=[]

for i in range(1,100):
    for b in range(2,i): 
        if i%b==0:
            break
    else:
        eleman.append(i)
print(eleman)
    

# alternative!!!
# =============================================================================
# sayi=abs(int(input('Lütfen bir sayı giriniz: ')))
# for bolen in range(2,sayi):
#     if sayi % bolen==0:
#         print(f'{sayi} asal değildir')
#         break
# else:
#     print(f'{sayi} asal sayıdır')
# =============================================================================



