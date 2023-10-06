import array as arr
import math
a = [1,2,3,4,5,6,7,8,9,10,15]
b = arr.array('i',a)
print(a)
for x in b:
    if x % 2 != 0 and x % 5 == 0:
        print(x)
#Cau c)
'''def is_prime(a):
    if a < 2:
        return False
    for i in range(2, math.sqrt(a) + 1):
        if a % i == 0:
            return False
    return True
def max_prime(b):
    for i in b:
        if is_prime(i):
            return max(i)
    else:
        return None
largest_prime = max_prime(b)
print("c) Số nguyên tố lớn nhất:", largest_prime)'''
 
'''Cau e'''
dem = 0
tong = 0
for z in b:
    if z % 2 != 0:
        dem += 1
        tong += z
z = tong/dem
print("e)Trung binh cac so le:",z )
'''Cau f'''
tich = 1
for y in b:
    if y % 2 != 0 and y % 3 == 0:
        tich *= y
print('f)Tich cac so le chia het cho 3:', tich)
#Cau g
def doi(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]
doi(b,0,-1)
print('g) Danh sach sau khi doi:',b)

