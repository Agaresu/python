import math
a = float(input("Nhap so a:"))
b = float(input("Nhap so b:"))
c = float(input("Nhap so c:"))
if a < 0 or b < 0:
    print("Ban nhap sai vui long nhap lai :)")
delta = b*2 - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta > 0:
    print("Phuong trinh co 2 nghiem: ")
    print("x1 = ", (-(b)+ math.sqrt(delta))/(2*a))
    print("x2 = ", (-(b)- math.sqrt(delta))/(2*a))
else:
    print("Phuong trinh co nghiem kep x1 = x2 = ", -(b / (2 * a)))