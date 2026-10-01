def kup_print(x):
    print(x * x)
def kup_returnt(x):
    return x * x
kup_print(2)
soru = kup_print(2)
print("küp", soru)
soru = kup_returnt(2)
print(soru + soru)


bilgiler = {"isim" : "messı", "gol" : 90, "asist" : 42}
for anahtar, deger in bilgiler.items():
    print(anahtar, ":", deger)

def selamla(isim="misafir", yas=18):
    print(f"merhaba {isim}! {yas} yaşındasın")
selamla("taha", 18)
selamla()


def fonksiyon(*args, **kwargs):
    carpim = 1
    for s in args:
        carpim *= s
    print("işte sayıların çarpımı", carpim)
    for an, deg in kwargs.items():
        print(f"{an} = {deg} ")
fonksiyon(2, 3, 4, isim="taha", şehir="van")

liste = ["ali","ayşe","mehemt","fatma"]
harf_5 = list(filter(lambda x: len(x) < 5, liste))
buyuk = map(lambda x:x.upper(), harf_5)
print(list(buyuk))

veriler = list(range(1, 11))
kupler = map(lambda x: x ** 3, list(filter(lambda x: x % 2 != 0, veriler)))
print(list(kupler))

kodlar = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yari = map(lambda x: x / 2, list(filter(lambda x: x < 50, kodlar)))
print(list(yari))

isimler = ["ali","ayşe", "mehemt", "fatma","ayhan"]
buyukler = map(lambda x: x.upper(), list(filter(lambda x: len(x) < 5, isimler)))
print(list(buyukler))

elde_var = [-10, 15, -20, 25, -30]
yeni_elde = map(lambda x: x*-1, list(filter(lambda x: x < 0, elde_var)))
son_hal = (list(yeni_elde) + list(filter(lambda x: x >0,elde_var)))
print(list(son_hal))

def kup(x):
    return x **3
def karma(func, sayi):
    return func(sayi) + 9
print(karma(kup, 2 ))


sozluk = {"elma": 10, "armut": 5, "ayva": 3}
try:
    meyve = input("bir meyve girin")
    print("adet:", sozluk[meyve])
except KeyError:
    print(f"{meyve} diye bir meyvemiz yok")

try:
    sayi = int(input("sayı giriniz"))
    sonuc = 10 / sayi
    print(f"10 / {sayi} = {sonuc}")
except ZeroDivisionError:
    print("HATA! sıfıra bölüm olmaz")
except ValueError:
    print("geçersiz karakter")

try:
    sayi = input("bir sayı gir")
    harf = input("bir harf gir")
    print(harf + sayi)
except (ValueError, ZeroDivisionError)as  e:
    print(f"HATA {e}")

try:
    sayi = int(input("bir sayı girin"))
    sonuc = 10 / sayi
    print(f"10 / {sayi} = {sonuc}")
except Exception as e:
    print(f"hata {e}")
finally:
    print("finally bloğu çalışıyor")


