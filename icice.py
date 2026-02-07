
username=input("kullanıcı adınızı giriniz: ")
password=input("şifrenizi giriniz: ")

dogru_username="admin"
dogru_password="12345"

if username==dogru_username:
    if password==dogru_password:
        print ("Login Success")
    else:
        print("password is wrong")
else:
    print("username is wrong")


