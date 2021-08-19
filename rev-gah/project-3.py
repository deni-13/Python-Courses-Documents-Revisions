
#kullanici girisi


giris_bilgileri = {"deniz":"j123"}
kullanici_adi = input("Kullanıcı Adı: ")
girildi_mi = False
if kullanici_adi in giris_bilgileri.keys():
  sifre = input("Şifre: ")
  if giris_bilgileri[kullanici_adi] == sifre:
    print("Giriş Başarılı")
    girildi_mi = True
  else: print("Şifre Yanlış")
else:
  print("Boyle bir kullanıcı bulunamadı")

menu = '''
1: Şifre Değiştir
2: Kullanıcı Adı Değiştir
3: Hesabı Sil
q: Çıkış Yap
'''
while girildi_mi:
  print(menu)
  secim = input("Lütfen seçim yapınız: ")

  if secim == "1":
    yeni_sifre = input("\nLütfen yeni şifrenizi giriniz: ")
    if len(yeni_sifre) >= 8:
      giris_bilgileri[kullanici_adi] = yeni_sifre
      print(f"\nYeni şifreniz {yeni_sifre} olarak değiştirildi!")
    else: print("Şifre en az 8 haneli olmalıdır")

  elif secim == "2":
    yeni_isim = input("\nLütfen yeni kullanıcı adınızı giriniz: ")
    giris_bilgileri[yeni_isim] = giris_bilgileri[kullanici_adi]
    del giris_bilgileri[kullanici_adi]
    kullanici_adi = yeni_isim
    print(f"\nKullanıcı adınız {yeni_isim} olarak değiştirildi!")

  elif secim == "3":
      silinecek_isim=input("gir--->")
    del giris_bilgileri[silinecek_isim]
    print("Hesabınız başarılı bir şekilde silindi")

  elif secim == "q":
    print("Görüşmek üzere...")
    break # girildi_mi = False

  else:
    print("Hatalı bir seçim yaptınız. Lütfen tekrar deneyin")