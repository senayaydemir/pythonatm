kartsifresi="2002"
bakiye="5000"
denemeHakki="3"
print("X Bankasına Hoşgeldiniz")
kart_islem_durumu=True
İslemDurumu = True
while İslemDurumu:
 girilenSifre=input("Kart Şifrenizi Giriniz:")
if girilenSifre != kartsifresi:
    print("Yanlış Şifre.Tekrar Deneyiniz.")
    denemeHakki -=1
    print(denemeHakki,"Deneme Hakkınız Kaldı")
    if denemeHakki == 0:
       print("Kartınız Bloklandı.Banka ile görüşün")
       İslemDurumu=False
else:
   while kart_islem_durumu:
      print("Giriş Yapıldı")    
      print("""
            Yapılacak İşlemi Seçiniz
            ------------------------
            1.Para Çekme
            2.Para Yatırma
            3.Bakiye Sorgulama
            4.Çıkış
            ------------------------
            """)
      islemNo =input("İşlem numarasını giriniz:")
      if islemNo =="4":
         print("Çıkış Yapıldı")
         İslemDurumu = False
         kart_islem_durumu = False
      elif islemNo == "3":
         print("Toplam Bakiye:",bakiye,"₺")
      elif islemNo == "2":
         yatırılacakmiktar=int(input("Yatırılacak Miktar:"))
         bakiye += yatırılacakmiktar
         print("İşlem Gerçekleşti")
      elif islemNo =="1":
         cekilecekmiktar = int(input("Çekilecek Miktar:"))
         if cekilecekmiktar > bakiye:
            print("Yetersiz Bakiye") 