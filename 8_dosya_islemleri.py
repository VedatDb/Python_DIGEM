import json
with open ("data.json", "r", encoding="utf-8") as file:
    data=json.load(file)

with open ("data.json", "w", encoding="utf-8") as file:
    KitapAdi=input("Kitap adı giriniz: ")
    Yazar=input("Yazar Adı giriniz: ")
    Yayin_tarihi=int(input("Yılı girinz: "))
    Fiyat=int(input("Fiyatını Giriniz: "))
    kategori=input("Kategori giriniz: ")
    Müsaitlik_Durumu=bool(input("Kitap müsait mi?: "))

    data.append (
        {
            "kitap_adi":KitapAdi,
            "yazar":Yazar,
            "Yılı":Yayin_tarihi,
            "Fiyat":Fiyat,
            "Kategori":kategori,
            "Müsaitlik Durumu":Müsaitlik_Durumu
        }  
    )

    json.dump(data,file,indent=4, ensure_ascii=False)
