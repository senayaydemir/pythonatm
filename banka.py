kartsifresi="2002"
bakiye="5000"
denemeHakki="3"
print("X Bankasına Hoşgeldiniz")
İslemDurumu = True
while İslemDurumu:
 girilenSifre=input("Kart Şifrenizi Giriniz:")
if girilenSifre != kartsifresi:
    print("Yanlış Şifre.Tekrar Deneyiniz.")
    denemeHakki -=1
    print(denemeHakki,"Deneme Hakkınız Kaldı")
    if denemeHakki == 0:
       print("Kartınız Bloklandı.Banka ile görüşün")
       
