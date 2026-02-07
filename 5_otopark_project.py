#Girdi kontrolü
import time


times=float(input("Otoparkta Ne kadar Süre Kalacaksınız (saat):"))
car_type=input("Araç tipi nedir? Otomobil / Motosiklet / Kamyon: ")
vip=input("VIP misiniz? (e/h): ")
no_ticket=input("Kayıp Bilet Var Mı? (e/h): ")

#Araç tipi kontrolü
if car_type=="otomobil":
    clock_price=30
elif car_type=="kamyon":
    clock_price=60
elif car_type=="motor":
    clock_price=20
else:
    print("Hatalı Giriş! Lütfen geçerli bir araç tipi giriniz")

#Ana hesaplama
if times <=1 and times>=0:
    total_price=0
    print("0-1 saat arası ücretsiz")
elif times>1:
    if times>10:
        total_price=(clock_price*times)*1.20
        if vip=="e" and no_ticket=="h":
            total_price=(clock_price*times)*0.70*1.20
            print (total_price, "%30 VIP indirim uygulandı")
        elif vip=="h" and no_ticket=="h":
            total_price=times*clock_price*1.20
            print("Toplam Tutar: ", total_price)
        elif no_ticket=="e":
            total_price=(clock_price*times*1.20)+200
            print("200 TL Kayıp Bilet Cezası!", total_price) 
    elif vip=="e" and no_ticket=="h":
        total_price=(clock_price*times)*0.70
        print (total_price, "%30 VIP indirim uygulandı")
    elif vip=="h" and no_ticket=="h":
        total_price=times*clock_price
        print("Toplam Tutar: ", total_price)
    elif no_ticket=="e":
        total_price=(clock_price*times)+200
        print("200 TL Kayıp Bilet Cezası!", total_price)
    else:
        print("Hatalı giriş")
       
else:
    print ("Hatalı süre girişi. Geçerli bir süre giriniz")  