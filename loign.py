username=input("Kullanıcı Adınızı Giriniz:")
password=input("Şifrenizi Giriniz:")

dogru_username="admin"
dogru_password="123456"

if username==dogru_username and password==dogru_password:
    print ("giriş başarılı")
else:
    print("mail veya şifre hatalı")
