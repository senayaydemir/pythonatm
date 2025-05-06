kartsifresi="2002"
bakiye="5000"
print("X Bankasına Hoşgeldiniz")
İslemDurumu = True
while İslemDurumu:
 girilenSifre=input("Kart Şifrenizi Giriniz:")
if girilenSifre != kartsifresi:
    print("Yanlış Şifre.Tekrar Deneyiniz.")
