from traceback import print_tb


yas=int(input("Yaşınızı giriniz: "))
ehliyet_yasi=int(input("Kaç yıldır ehliyete sahipsiniz?: "))
hasar_gecmisi=input("Hasar geçmişiniz var mı? (e/h): ")
sehir_ici=input("Şehir içinde mi kullanacaksınız? (e/h)")
sure=int(input("Kaç gün kullanacaksınız?"))

if sehir_ici=="h":
    mesaj1=print("Ek sehir dışı kullanım depozitosu ödeyiniz")
elif sure>=10:
    mesaj2=print ("Ek kullanım süresi depozitosu ödeyiniz")
elif sehir_ici=="h" and sure>=10:
    mesaj3=print ("Toplamda 2 adet ek depozito ödeyiniz")

if yas>=25 and ehliyet_yasi>=5 and hasar_gecmisi=="h":
    print("Araç kiralayabilirsiniz")
    if sehir_ici=="h" and sure<10:
        print("Araç kiralayabilirsiniz", mesaj1)
    elif sure>=10 and sehir_ici=="e":
        print("Araç kiralayabilirsiniz", mesaj2)
    elif sehir_ici=="h" and sure>=10:
        print("Araç kiralayabilirsiniz", mesaj3)
elif yas>=25 and (ehliyet_yasi<=5 or hasar_gecmisi=="h"):
    print("Depozito ücreti ödeyerek araç kiralayabilirsiniz")
    if sehir_ici=="h":
        print("Depozito ücreti ödeyerek araç kiralayabilirsiniz", mesaj1)
    elif sure>=10:
        print("Depozito ücreti ödeyerek araç kiralayabilirsiniz", mesaj2)
    elif sehir_ici=="h" and sure>10:
        print("Depozito ücreti ödeyerek araç kiralayabilirsiniz", mesaj3)
else:
    print("Araç kiralayamazsınız")

    
    
#kullanım : şehir içi veya şehir dışıç.. şehir dışı ise ek dpo... 10 günden fazla ise ek depozito
