yas=int(input("Yaşınızı giriniz: "))
acil=input("Acil mi? (e/h)")
kronik=input("Kronik rahatıszlığı var mı? (e/h)")

if yas>=65 or acil=="e" or kronik=="e":
    print("Yüksek öncelikli hasta")
elif yas>=65 and kronik=="e"and acil=="h":
    print("Öncelikli hasta")
else:
    print("Normal hasta")