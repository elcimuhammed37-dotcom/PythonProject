isim = input("Adınızı girin: ")
yas = int(input("yaşınızı girin: "))
boy = float(input("boyunuzu metre cinsinden: "))
yas_sonra = yas + 5
boy_sonra = boy * 2
print("\n---  hesaplama sonuçları ---")
print(f"merhaba {isim} ")
print(f"şu anki yaşınız: {yas}")
print(f"5 yıl sonraki yaşınız: {yas_sonra}")
print(f"boyunuzum 2 katı : {boy_sonra} metre")
print("_________________________")

ogrenciler = {"ali":[80, 75, 45], "ahmet":[90, 60, 55],"ayşe":[45, 39,81]}
def not_analiz(notlar):
    ort = sum(notlar) / len(notlar)
    en_yuksek = max(notlar)
    en_dusuk = min(notlar)
    return ort, en_yuksek, en_dusuk
def tablo_yazdir():
    print("\n -----SINIF NOT ANALİZİ -----")
    for i, (isim,notlar) in enumerate(ogrenciler.items(), start=1):
        ort, en_yuksek, en_dusuk = not_analiz(notlar)
        print(f"{i}.{isim} --- ORTALAMA {ort:.2f}| EN YÜKSEK {en_yuksek}| EN DÜŞÜK {en_dusuk}")
def not_ekle():
    isim = input("not eklemek yada listeye yeni öğrenci için isim ekleyin")
    try:
        notu = int(input("bir not girin"))
    except ValueError:
        print("not sayısal olmalı")
        return
    if isim in ogrenciler:
        ogrenciler[isim].append(notu)
    else:
        ogrenciler[isim] = [notu]
        print(f"{isim} için not eklendi")
while True:
    print(f"\n MENÜ ")
    print("1 - mevcut notları oku")
    print("2 - dosyaya ekleme yap")
    print("3 - çıkış ")

    try:
        secim = int(input("seçimi girin (1/2/3)"))
    except ValueError:
        print("lütfen seçim için sayı girin")
        continue
    if secim==1:
        tablo_yazdir()
    elif secim==2:
        not_ekle()
    elif secim==3:
        print("PROGRAMDAN ÇIKILIYOR")
        break
    else:
        print("lütfen geçerli bir sayı girin")

ogrenciler = {"ali":[80, 90, 75], "yaren":[45, 75,80], "kahraman":[60, 50, 40]}
toplamlar = list(map(lambda x: (x[0], sum(x[1])), ogrenciler.items()))
print("toplam notlar:", toplamlar)

ogrenciler = {"ali":[80,90,72], "türkü":[67,72,90],"mert":[32,98,51]}

def not_ekle():
    while True:
        isim = input("bir isim girin").strip()
        if not isim:
            print("isim boş olamaz")
            continue
        try:
            notu = int(input("bir not girin"))
            if not 0 <= notu <= 100:
                print("not 0 ile 100 arasında olmalı")
                continue
        except ValueError:
            print("not sayısal olmalı")
            continue
        if isim in ogrenciler:
            ogrenciler[isim].append(notu)
        else:
            ogrenciler[isim] = [notu]
        print(f"{isim} için {notu} eklendi")
        break
def notlari_gor():
    isim = input("aradığınız ismi girin ").strip()
    if isim in ogrenciler:
        print(f"{isim} için notlar {ogrenciler[isim]}")
    else:
        print(f"{isim} listede bulunmuyor")
def ortalama_hesaplama():
    ortalamalar = []
    for isim, notlar in ogrenciler.items():
        ort = sum(notlar) / len(notlar)
        ortalamalar.append((isim, ort))
        ortalamalar.sort(key=lambda x: x[1], reverse=True)
        for isim, ort in ortalamalar:
            print(f"{isim} --- ortalama {ort:.2f}")

def en_yuksek_en_dusuk():
    isim = input("en yüksek ve düşük notlarını görmek istediğiniz öğrencinin ismini girir")
    if isim in ogrenciler:
        notlar = ogrenciler[isim]
        yuksek = max(notlar)
        dusuk = min(notlar)
        print(f"{isim} adlı öğrencinin en yüksek ve düşük notları {yuksek} {dusuk}")
    else:
        print(f"{isim} adlı birisi listede bulunmuyor")


def menu():
    while True:
        print("---öğrenci not sistemine hoşgeldiniz---")
        print("1- NOT EKLE")
        print("2- MEVCUT NOTLARI GÖR")
        print("3- ORTALAMALARI GÖRÜN")
        print("4- EN YÜKSEK VE DÜŞÜK NOT")
        print("5- ÇIKIŞ")
        try:
            secim = int(input("kullanmak istediğiniz özelliğin numarasını yazın"))
        except ValueError:
            print("lütfen bir sayı girin")
            continue
        if secim==1:
            not_ekle()
        elif secim==2:
            notlari_gor()
        elif secim==3:
            ortalama_hesaplama()
        elif secim==4:
            en_yuksek_en_dusuk()
        elif secim==5:
            print("programdan çıkılıyor ...")
            break
        else:
            print("geçersiz seçim")
menu()

