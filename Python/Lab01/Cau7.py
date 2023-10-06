import math
n = int(input("Nhap n so nguyen: "))
tong = 0
if n < 0:
    print("Ban nhap sai vui long nhap lai")
    
else:
    for i  in range (1,n+1):
        tong += math.sqrt(i)
    print("Tong can bac 2: ", tong)