import math
def XetSoNguyenTo(n):
    if (n < 2):
        return False
 
    So = int(math.sqrt(n))
    for i in range(2, So + 1):
        if (n % i == 0):
            return False
    return True
 
n = int(input("Nhap khoang n = "))
print ("Tat ca cac so nguyen to trong khoang ", n, "là:")
sb = ""
if (n >= 2):
    sb = sb + "2" + " "
for i in range (3, n+1):
    if (XetSoNguyenTo(i)):
        sb = sb + str(i) + " "
    i = i + 2
print(sb)