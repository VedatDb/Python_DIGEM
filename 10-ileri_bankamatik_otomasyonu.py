import json
import mailbox
import random

with open ("bankamatik.json", "r", encoding="utf-8") as file:
    data=json.load(file)

while True:
    k_mail=input("Mail Adresinizi Giriniz: ")
    giris=False
    for user in data: 
        if user ["mail"]==k_mail:
            k_password=input("Şifrenizi Girinizi: ")

            hesap_var=False
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
                new_mail=input("Mail adresinizi girinizi: ")
                new_password=input("Şifreinizi giriniz: ")
                hesap_var=False
                for user in data:
                    if user["mail"]==new_mail:
                        print("Bu mail adresi zaten kullanılıyor")
                        hesap_var=True
                        break
                
                if hesap_var==False:
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