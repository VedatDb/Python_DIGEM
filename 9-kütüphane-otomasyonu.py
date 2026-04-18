import json

with open ("data.json", "r", encoding="utf-8") as file:
    data=json.load(file) 

while True:
    print("""
    1- Kitap Ekle
    2- Kitap Sil
    3- Kitap Vermek
    4- Kitap Listele
    5- Çıkış
    """)
    secim=input("Seçiminizi yapınız: ")
    if secim=="1":
        with open ("data.json", "w", encoding="utf-8") as file:
            kitapAdi=input("Kitap Adını Giriniz: ")
            Yazar=input("Yazar Adını Giriniz: ")
            Yayin_yili=int(input("Yayın Yılını Giriniz: "))
            fiyat=int(input("Fiyatını Giriniz: "))
            kategori=input("Kitabın Türünü Giriniz: ")
            Musaitlik_Durumu=bool(input("Kitap Müsait mi? "))
            
            data.append (
            {
                "kitap_adi":kitapAdi,
                "yazar":Yazar,
                "Yılı":Yayin_yili,
                "Fiyat":fiyat,
                "Kategori":kategori,
                "Müsaitlik Durumu":Musaitlik_Durumu
            }
            )
         

            json.dump(data,file,indent=4, ensure_ascii=False)
    
    elif secim=="4":
        for kitap in data:
            print("-"*20)
            print (f"Kitap Adı", kitap["kitap_adi"])
            print (f"Yazar:", kitap["yazar"])
            print (f"Yılı", kitap["Yılı"])
            print (f"Fiyat", kitap["Fiyat"])
            print (f"Kategori", kitap["Kategori"])
            if kitap["Müsaitlik Durumu"]:
                print("Müsaitlik Durumu: Uygun")
            else:
                print("Müsaitlik Durumu: Uygun Değil")
    
    elif secim=="2":
    
        with open ("data.json", "w", encoding="utf-8") as file:
           
            silinecek_kitap=input("Silenecek Kitap Adını Giriniz: ")
            
            for kitap in data:
                if kitap ["kitap_adi"]==silinecek_kitap:
                    data.remove(kitap)
                    print("Kitap Silindi")
                    break
            json.dump(data,file,indent=4, ensure_ascii=False)

    elif secim=="3":
    
        with open ("data.json", "w", encoding="utf-8") as file:

            kitap_ver=input (" Almak istediğiniz kitap adını giriniz: ")
            for kitap in data:
                if kitap["kitap_adi"]==kitap_ver:
                    if kitap["Müsaitlik Durumu"]==True:
                        print("Kitap Müsait")
                        kitap["Müsaitlik Durumu"]==False
                    else:
                        print("Kitap Müsait Değil")
            json.dump(data,file,indent=4, ensure_ascii=False)
                

                    
