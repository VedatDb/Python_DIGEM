import json
import mailbox
import random
from re import S

with open ("bankamatik.json", "r", encoding="utf-8") as file:    
    data=json.load(file)

while True:
    k_mail=input("Mail Adresinizi Giriniz: ")
    giris=False
    for user in data: 
        if user ["mail"]==k_mail:
            k_password=input("Şifrenizi Girinizi: ")
          
            if user["password"]==k_password:
                print("Giriş Başarılı")
                giris=True
                break
            else:
                print("Şifreniz Yanlış")
                giris=False
                break
             
    if giris==False:
            
        secim=input("Yeni bir hesap oluşturmak ister misin? (e/h)")
        if secim=="e":
            new_mail=input("Mail adresinizi giriniz: ")
            new_password=input("Şifrenizi giriniz: ")
        
            hesap_var=False
            for user in data:
                if user["mail"]==new_mail:
                    print("Bu mail adresi zaten kullanılıyor")
                    hesap_var=True
                    break
                    
            if hesap_var==True:
                break
            else:
                with open("bankamatik.json","w", encoding="utf-8") as file:
                    data.append({
                        "mail":new_mail,
                        "password":new_password,
                        "bakiye":{
                                "TL": 0,
                                "USD": 0,
                                "EUR": 0,
                                "GOLD": 0
                            }

                    })
                    json.dump(data,file,indent=4, ensure_ascii=False)
                    print("Hesap oluşturuldu.")
        else:
            print("Uygulamadan Çıkılıyor...")
            break

    elif giris==True:
        while True:
            print("""
(1) Bakiye Görüntüle
(2) Para Çek
(3) Para Yatırıma
(4) Döviz Çevirme
(5) Çıkış
        """)
            secim=input("Seçim Yapınız")
            
            if secim=="1":
                print(f"Bakiyeniz: {user['bakiye']['TL']} TL")
                print(f"Bakiyeniz: {user['bakiye']['USD']} USD")
                print(f"Bakiyeniz: {user['bakiye']['EUR']} EUR")
                print(f"Bakiyeniz: {user['bakiye']['GOLD']} GOLD")
            elif secim=="2":
                miktar=int(input("Çekmek istediğiniz miktarı giriniz: "))
                if miktar<=user['bakiye']['TL']:
                    user['bakiye']['TL']-=miktar
                    print(f"Çekilen tutar: {miktar} TL")
                    print(f"Kalan bakiye: {user['bakiye']['TL']} TL")
                    with open("bankamatik.json", "w", encoding="utf-8") as file:
                        json.dump(data,file,indent=4, ensure_ascii=False)
                else:
                    print("Bakiyeniz yetersiz")
            elif secim=="3":
                miktar=int(input("Yatırmak istediğiniz miktarı giriniz: "))
                user['bakiye']['TL']+=miktar
                print(f"Yatırdığınız miktar: {miktar} TL")
                print(f"Yeni bakiye: {user['bakiye']['TL']} TL")
                with open("bankamatik.json", "w", encoding="utf-8") as file:
                    json.dump(data,file,indent=4, ensure_ascii=False)
            elif secim=="5":
                print("Uygulamadan Çıkılıyor... ")
                break
            else:
                print("Hatalı tuşlama")
                continue