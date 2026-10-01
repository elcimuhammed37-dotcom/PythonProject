

meyveler = {"elma": 7, "armut": 3, "kivi": 6, "pancar": 4, "muz": 8}
buyukler = list(filter(lambda item: item[1] > 5, meyveler.items()))
toplam = sum(item[1] for item in buyukler)
siralilar = list(sorted(buyukler, key=lambda item: item[1], reverse=True))
for isim, adet in siralilar:
    print(f"{isim}: {adet}")
print(f"toplam: {toplam}")