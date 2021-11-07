f=open("work.txt","w") #yazma modunda acmak
f.write("text")
f.close()


f=open("work.txt","r")
print(f.read())   #terminale yaziyi bastirma
f.close()

#%%
#without file close 

with open("g.txt","w") as file:
    file.write("hello")
with open("g.txt","a") as file: #yeni biseyler ekleme
    file.write(" "+  "hi baby")
    
with open("g.txt","r") as file:
    d=file.read()