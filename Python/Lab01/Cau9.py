n = int(input("Nhap so n: "))
if n < 0:
    print("Ban nhap sai vui long nhap lai")
else:
    for i in range (1, n):
        n *= i
    print("Luy thua cua n: ",n)