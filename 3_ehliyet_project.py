yas=int(input("yaşın"))


#18 yaş, sürüş için engeliniz var mı, sınavdan 70,  

if yas>=18:
    print("Yaşınız uygun, sürüş için engeliniz var mı?")
    sağlik_durumu=input("Sürüş için engeliniz var mı?: e/h")

    if sağlik_durumu=="h":
        print("Sürüş için bir engeliniz yok")
        ilksinav=int(input("Teorik Sınavdan kaç aldınız?"))
        if ilksinav>=70:
            print ("Puanınız yeterli")
            uygulamaSinav=input("Uygulama Sınavını Geçtiniz mi? e/h")
            if uygulamaSinav=="e":
                print("Tebrikler ehliyet alabilirsiniz")
            else:
                print("Tekrar uygulama sınavına giriniz")
        else:
            print ("Tekrar teorik sınava giriniz")
    else:
        print("Engeliniz var , ehliyet alamazsınız")
else:
    print("Yaşınız uygun değil")




