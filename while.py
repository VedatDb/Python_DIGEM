from random import randint
tahmin_sayi=randint(1,10)
hak=3
while True:
    tahmin=int(input("1-10 arasında bir sayı giriniz: "))
    hak=hak-1
    if hak==0:
        print("Game over")
        print("Tutulan sayı", tahmin)
        break
    else:           
        if tahmin==tahmin_sayi:
            print("Tebrikler! Sayıyı bildiniz")
            break
        elif tahmin>tahmin_sayi:
            print("Daha küçük bir sayı")
        elif tahmin<tahmin_sayi:
            print("Daha büyük bir sayı")
        else:
            print("Yanlış tuşlama")
        print(hak, "Hakkınız kaldı")
    