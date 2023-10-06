import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-LL7P35M\\SQLEXPRESS;DATABASE=QLSinhVien;Trusted-Connection = yes;')
cursor =  conn.cursor()
cursor.execute("Select @@version")

db_version = cursor.fetchone()
conn.close()
print("Bạn đang dùng hệ quản trị CSDL SQL server phiên bản: ",db_version)