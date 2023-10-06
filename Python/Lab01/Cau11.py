ss = int(input("Nhap so giay: "))
giay = ss%86400%3600%60
ngay = ss//86400
gio = ss%86400//3600
phut = ss%86400%3600//60
print(ngay ,": ",gio,":",phut,": ",giay,": ")