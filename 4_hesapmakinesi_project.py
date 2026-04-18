sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))

islem=input("İşlemi seçiniz: +, -, *, /, %, **: ")

if islem=="+" or islem=="toplama":
    print("Toplama: ", sayi1+sayi2)
elif islem=="-":
    print("Çıkarma: ", sayi1-sayi2)
elif islem=="*":
    print("Çarpma: ", sayi1*sayi2)
elif islem=="/":
    if sayi2==0:
        print("Sıfıra bölünemez")
    else:
        print("Bölme: ", round(sayi1/sayi2, 2))
elif islem=="%":
        if sayi2==0:
            print("Sıfıra bölünemez")
        else:   
            print("Mod: ", round (sayi1%sayi2, 2))
elif islem=="**":
    print("Üs: ", sayi1**sayi2)
else:
    print("Geçersiz işlem") 