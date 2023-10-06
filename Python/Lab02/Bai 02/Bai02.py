f = open("Bai 02/sinhvien.txt",mode = "r", encoding= 'utf-8')
read = f.readlines()
listSv = []
sv = []
for i in read:
    if i not in listSv:
        listSv.append(i.strip())
print("\nDanh Sách Sinh Viên:\n",listSv)
# Cau 2: Sắp xếp danh sách sinh viên tăng/giảm theo họ tên
#Sắp xếp danh sách sinh viên tăngtheo họ tên
listSv.sort(key=lambda x: x.split(',')[1])  
print("\nDanh sách sinh viên theo họ tên tăng dần:")
print('\n'.join(listSv)) 

#Sắp xếp danh sách sinh viên giảm theo họ tên
listSv.sort(key=lambda x: x.split(',')[1],reverse=True) 
print("\nDanh sách sinh viên theo họ tên giảm dần:")
print('\n'.join(listSv))  
f.close()
