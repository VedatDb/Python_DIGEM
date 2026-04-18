kullanicilar= {
    
    "kerem":{"sifre":"123","bakiye": 160},
    "berivan":{"sifre": "6057", "bakiye":20000},
    "mizgin":{"sifre":"1946", "bakiye":10000}

    }

username=input("Kullanıcı adını giriniz: ")


if username in kullanicilar:
    hak=3
    while hak>0:
        sifre=input("şifrenizi giriniz:")
        if sifre==kullanicilar[username]["sifre"]:
            print("hesaba giriş yapıldı")
            break
        else:
            hak-=1
            print("şifreniz yanlış")
    if hak==0:
        print("kart bloke")
    else:
        bakiye=kullanicilar[username]["bakiye"]
        
        while True:
            print("""
            (1)Bakiye Görüntüle
            (2)Para Çek
            (3) Para Yatırıma
            (4) Çıkış
            """)
            secim=input("Secim yapınızız")
        


            
            if secim=="1":
                print(f"bakiyeniz: {bakiye}")
            elif secim=="2":
                miktar=int(input("Çekmek istediğiniz miktarı giriniz"))
                if miktar<=bakiye:
                    print(f"Çekilen tutar: {miktar}")
                    bakiye=bakiye-miktar
                    print(f"Kalan tutar: {bakiye}")
                else:
                    print("yeterli bakiye bulunmamaktadır")
            elif secim=="3":
                yatirim=int(input("Yatırmak istediğiniz miktarı girin: "))
                print(f"Yatırdığınız miktar: {yatirim}")
                bakiye=bakiye + yatirim
                print(f"Yeni bakiye: {bakiye} ")

            elif secim=="4":
                print("Çıkış yaptınız")
                break
            else:
                print("Hatalı tuşlama")
            