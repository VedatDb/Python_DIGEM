sure=int(input("Otoparkta Ne kadar Süre Kalacaksınız (saat):"))
arac=input("Araç tipi nedir? Otomobil / Motosiklet / Kamyon : ")
vip=input("VIP misiniz? (Evet/Hayır): ")
kayip_bilet=input("Kayıp Bilet Var Mı? (Evet/Hayır): ")
saatlik_ucret_oto = 30
saatlik_ucret_kamyon = 60
saatlik_ucret_motosiklet = 20


if sure<=1:
    print("0 TL. 0-1 Saat arası ücretsiz otopark")
elif sure<0:
    print("Hatalı Giriş! Lütfen geçerli bir süre giriniz")
elif arac=="Otomobil":
    if sure>10:
        if vip=="evet":
            print(f"{saatlik_ucret_oto*sure*0.70*1.20} TL. %20 uzun süre zammı ve %30 VIP indirimi uygulandı")
        elif vip=="hayır" and kayip_bilet =="evet":
            print (f"{saatlik_ucret_oto*sure*1.20 + 200} TL. %20 uzun süre zammı ve 200 TL kayıp bilet ücreti uygulandı")
        elif vip=="hayır" and kayip_bilet =="hayır":
            print (f"{saatlik_ucret_oto*sure*1.20} TL. %20 uzun süre zammı uygulandı")        
    elif sure<=10:
        if vip=="evet":
            print(f"{saatlik_ucret_oto*sure*0.70} TL. %30 VIP indirimi uygulandı")
        elif vip=="hayır" and kayip_bilet =="evet":
            print (f"{saatlik_ucret_oto*sure + 200} TL. 200 TL kayıp bilet ücreti uygulandı")
        elif vip=="hayır" and kayip_bilet =="hayır":
            print (f"{saatlik_ucret_oto*sure} TL.")     
elif arac=="Motosiklet":
    if sure>10:
        if vip=="evet":
            print(f"{saatlik_ucret_motosiklet*sure*0.70*1.20} TL. %20 uzun süre zammı ve %30 VIP indirimi uygulandı")
        elif vip=="hayır" and kayip_bilet =="evet":
            print (f"{saatlik_ucret_motosiklet*sure*1.20 + 200} TL. %20 uzun süre zammı ve 200 TL kayıp bilet ücreti uygulandı")
        elif vip=="hayır" and kayip_bilet =="hayır":
            print (f"{saatlik_ucret_motosiklet*sure*1.20} TL. %20 uzun süre zammı uygulandı")
    elif sure<=10:
        if vip=="evet":
            print(f"{saatlik_ucret_motosiklet*sure*0.70} TL. %30 VIP indirimi uygulandı")
        elif vip=="hayır" and kayip_bilet =="evet":
            print (f"{saatlik_ucret_motosiklet*sure + 200} TL. 200 TL kayıp bilet ücreti uygulandı")
        elif vip=="hayır" and kayip_bilet =="hayır":
            print (f"{saatlik_ucret_motosiklet*sure} TL.")
elif arac=="Kamyon":
    if sure>10:
        if vip=="evet":
            print(f"{saatlik_ucret_kamyon*sure*0.70*1.20} TL. %20 uzun süre zammı ve %30 VIP indirimi uygulandı")
        elif vip=="hayır" and kayip_bilet =="evet":
            print (f"{saatlik_ucret_kamyon*sure*1.20 + 200} TL. %20 uzun süre zammı ve 200 TL kayıp bilet ücreti uygulandı")
        elif vip=="hayır" and kayip_bilet =="hayır":
            print (f"{saatlik_ucret_kamyon*sure*1.20} TL. %20 uzun süre zammı uygulandı")
    elif sure<=10:
        if vip=="evet":
            print(f"{saatlik_ucret_kamyon*sure*0.70} TL. %30 VIP indirimi uygulandı")
        elif vip=="hayır" and kayip_bilet =="evet":
            print (f"{saatlik_ucret_kamyon*sure + 200} TL. 200 TL kayıp bilet ücreti uygulandı")
        elif vip=="hayır" and kayip_bilet =="hayır":
            print (f"{saatlik_ucret_kamyon*sure} TL.")
else:
    print ("Hatalı araç seçimi! Lütfen aracınızı seçiniz")