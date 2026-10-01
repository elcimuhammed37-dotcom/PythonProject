from logging import getLogger

while True:

    isim = input("adınızı girin: ")
    yas = int(input("yaşınızı girin: "))
    boy = float(input("boyunuzu girin: "))
    yas_sonra = yas + 5
    boy_iki = boy * 2
    print("\n--- hesaplama sonuçları ---")
    print(f"Merhaba: {isim} ")
    print(f"şu anki yaşınız: {yas}")
    print(f"5 yıl sonraki yaşınız: {yas_sonra}")
    print(f"boyunuzun iki katı : {boy_iki}) metre")
    print("____________________\n")
    devam = input("Başka bir hesaplama yapmak istermsiniz? (evet/hayır): ").lower()
    if devam != "evet":
        print("programdan çıkılıyor.Hoşçakal!")
        break

def not_analiz(ogrenciler):
    sonuc = {"geçenler":[],"kalanlar":[]}
    for ogrenci in ogrenciler:
        isim = ogrenci[0].strip().title()
        notu = ogrenci[1]
        if notu >= 50:
            sonuc["geçenler"].append(isim)
        else:
            sonuc["kalanlar"].append(isim)
    return sonuc
ogrenci_listesi = [("tahir",70),("harran",56),("piraye",30),("erhan",25)]
sonuc = not_analiz(ogrenci_listesi)
print("geçenler:", sonuc["geçenler"])
print("kalanlar:", sonuc["kalanlar"])
def not_analiz_ortalama(ogrenciler):
    sonuc = {"geçenler":[],"kalanlar":[],"ortalama":[]}
    toplam = 0
    for ogrenci in ogrenciler:
        isim = ogrenci[0].strip().title()
        notu = ogrenci[1]
        toplam += notu
        if notu >= 50:
            sonuc["geçenler"].append(isim)
        else:
            sonuc["kalanlar"].append(isim)
    if len(ogrenciler) > 0:
        sonuc["ortalama"] = toplam / len(ogrenciler)
    return sonuc
ogrenci_panosu = [("tahir",70),("hayriye",65),("hasan",45),("feride",85),("arif",50)]
sonuc = not_analiz_ortalama(ogrenci_panosu)
print("geçenler",sonuc["geçenler"])
print("kalanlar",sonuc["kalanlar"])
print("ortalama",sonuc["ortalama"])
def not_analiz_v3(ogrenciler):
    sonuc = {"geçenler":[],"kalanlar":[],"ortalama":[],"en yüksek":None,"en düşük":None,"geçen sayısı":0,"kalan sayısı":0}
    if not ogrenciler:
        return sonuc
    toplam = 0
    en_yuksek = ("",float("-inf"))
    en_dusuk = ("",float("inf"))
    for isim, notu in ogrenciler:
        isim = isim.strip().title()
        toplam += notu
        if notu >= 50:
            sonuc["geçenler"].append(isim)
        else:
            sonuc["kalanlar"].append(isim)
        if notu > en_yuksek[1]:
            en_yuksek = (isim,notu)
        if notu < en_dusuk[1]:
            en_dusuk = (isim,notu)
    sonuc["ortalama"] = toplam / len(ogrenciler)
    sonuc["en yüksek"] = en_yuksek
    sonuc["en düşük"] = en_dusuk
    sonuc["geçen sayısı"] = len(sonuc["geçenler"])
    sonuc["kalan sayısı"] = len(sonuc["kalanlar"])
    return sonuc
ogrenci_notlar = [("cevahir",75),("fevzi",60),("ismet",75),("mustafa",90),("enver",45),("abdulhamid",45)]
sonuc = not_analiz_v3(ogrenci_notlar)
print("======NOT ANALİZİ RAPORU=======")
print(f"geçenler ({sonuc["geçen sayısı"]} kişi):{",".join(sonuc["geçenler"])}")
print(f"kalanlar ({sonuc["kalan sayısı"]} kişi):{",".join(sonuc["kalanlar"])}")
print("-"*30)
print(f"ortalama not {sonuc["ortalama"]:.2f}")
print(f"en yüksek not {sonuc["en yüksek"][0]} {sonuc["en yüksek"][1]}")
print(f"en düşük not {sonuc["en düşük"][0]} {sonuc["en düşük"][1]}")
print("="*30)

urunler = []
fiyatlar = []
for i in range(3):
    urun = input("ürün adı:")
    fiyat = int(input("ürün fiyatını girin:"))
    urunler.append(urun)
    fiyatlar.append(fiyat)
print("ÜRÜNLER".ljust(10), "FİYATLAR".rjust(5))
print("-"*15)
for urun, fiyat in zip(urunler, fiyatlar):
    renk = "\033[91m" if fiyat > 10 else "\033[92m"
    print(urun.ljust(10), renk + str(fiyat).rjust(5) + "\033[0m")
urunler = ["elma","armut","muz","çilek","ayva"]
gelir = []
gider = []
for urun in urunler:
    while True:
        try:
            g = float(input(f"{urun} için satış rakamı belirleyin:"))
            gelir.append(g)
            break
        except ValueError:
            print("lütfen sayı girin")
    while True:
        try:
            z = float(input(f"{urun} için giderleri girin:"))
            gider.append(z)
            break
        except ValueError:
            print("lütfen sayısal bir değer girin")
yesil = "\033[92m"
kirmizi = "\033[91m"
sifirla = "\033[0m"
print("ürün".ljust(10), "gelir".rjust(6),"gider".rjust(6),"kar".rjust(6))
print("-"*30)
for u,g,z in zip(urunler, gelir, gider):
    kar = g - z
    renk = yesil if kar >=0 else kirmizi
    print(u.ljust(10), str(g).rjust(6), str(z).rjust(6), f"{renk}{kar}{sifirla}".rjust(6))

with open("mini_muhasebe.txt","w") as dosya:
    dosya.write("ÜRÜN".ljust(10) + "GELİR".rjust(6) + "GİDER".rjust(6) + "KAR".rjust(6))
    dosya.write("-"*30 + "\n")
    for u,g,z in zip(urunler, gelir, gider):
        kar = g - z
        renk = yesil if kar >=0 else kirmizi
        dosya.write(str(u).ljust(10) + str(g).rjust(6) + str(z).rjust(6) + (renk) +str(kar).rjust(6) + sifirla)
        dosya.write("-"*30 + "\n")
print("\nTablo 'mini_muhasebe.txt' dosyasına kaydedildi.")