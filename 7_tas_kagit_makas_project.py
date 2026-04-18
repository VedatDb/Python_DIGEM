import random
secenekler=["taş", "kağıt", "makas"]
kullanici_puan=0
bilgisayar_puan=0
while True:
    secim=input("Seçiminizi giriniz: (taş/kağıt/makas veya çıkış için q yazınız): ").lower()
    if secim=="q":
        print("Oyunu sonlandırdınız.")
        break
    
    if secim not in secenekler:
        print(f"Geçersiz seçim. Lütfen tekrar giriniz.\n")
        continue
    bilgisayar=random.choice(secenekler)
    
    print(f"Senin seçimin: {secim} ve Bilgisayarın seçimi: {bilgisayar}")
    
    if secim==bilgisayar:
        print("Berabere")
    elif secim=="makas" and bilgisayar=="taş":
        print(f"Bilgisayar Kazandı!")
        bilgisayar_puan+=1
    elif secim=="taş" and bilgisayar=="kağıt":
        print(f"Bilgisayar Kazandı!")
        bilgisayar_puan+=1
    elif secim=="kağıt" and bilgisayar=="makas":
        print(f"Bilgisayar Kazandı!")
        bilgisayar_puan+=1
    elif secim=="makas" and bilgisayar=="kağıt":
        print(f"Kazandınız!")
        kullanici_puan+=1
    elif secim=="taş" and bilgisayar=="makas":
        print(f"Kazandınız!")
        kullanici_puan+=1
    elif secim=="kağıt" and bilgisayar=="taş":
        print(f"Kazandınız!")
        kullanici_puan+=1
    print(f"Senin puanın {kullanici_puan} ve Bilgisayarın puanı {bilgisayar_puan}\n")    
    
    if kullanici_puan==3 or bilgisayar_puan==3:
        print(f"Oyun Bitti!")
        if kullanici_puan==3:
            print("Tebrikler! Kazandınız...")
        else:
            print("Bilgisayar Kazandı!")
        break