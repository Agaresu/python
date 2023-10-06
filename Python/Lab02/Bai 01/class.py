from datetime import datetime
class SinhVien:
    #biến của lớp, chung cho tất cả đối tượng thuộc lớp
    truong = 'Đại Học Đà Lạt'
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo #thuoc tinh private
        self._hoTen = hoTen #thuoc tinh private
        self._ngaySinh = ngaySinh #thuoc tinh private
    #cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường nào
    @property
    def maSo(self):
        return self._maSo
    #cho phép thay đổi giá trị thuộc tính maSo
    @maSo.setter
    def maSo(self,maSo):
        if self.laMaSoHopLe(maSo):
            self._maSo = maSo
    #phương thức tĩnh: các phương thức không truy xuất gì đến thuộc tính, hành vi của lớp
    #những phương thức này không cần truyền tham số mặc định self
    #đấy không phải là một hành vi (phương thức) của 1 đối tượng thuộc lớp
    @staticmethod
    def laMaSoHopLe(maSo : int):
        return len(str(maSo)) == 7
    #phương thức của lớp, chỉ truy xuất tới các biến thành viên của lớp
    #không truy xuất được các thuộc tính của đối tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    #tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"
    #hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")
class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
    def themSinhVien(self, sv : SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    def timSVTheoMssv(self, mssv : int):
        return[sv for sv in self.dssv if sv.mssv == mssv]
    def timVTSVTheoMssv(self, mssv : int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i 
            return -1
    def xoaSVTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSVTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    #Tim Sinh Vien ten Nam
    def timSvTheoTen(self, ten: str):
        return[ten for ten in self.dssv if self.hoTen == "Nam"]
    #Tim sinh vien sinh truoc ngay 15/6/2000
    def timSVSinhTruocNgay(self, ngaySinh : datetime):
        return[ngaySinh for ngaySinh in self.dssv if self.ngaySinh < "15/6/2000"]
sv1 = SinhVien(111,"Nguyễn Dương Công Bảo", datetime.strptime("28/10/2003", "%d/%m/%Y"))
sv2 = SinhVien(404,"Nguyễn Phúc Hoàng Anh", datetime.strptime("27/07/2002", "%d/%m/%Y"))
dssv = DanhSachSV()
dssv.themSinhVien(sv1)
dssv.themSinhVien(sv2)
dssv.xuat()
vt = dssv.timSVTheoMssv(404)
print(f"Sinh vien o vi tri thu {vt + 1} trong danh sach")
for sv in vt:
   print("Danh sach sau khi loc: ", sv)



