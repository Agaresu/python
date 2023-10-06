import math
class PhanSo:
    def __init__(self, tu = 1, mau = 1) -> None:
        self.tu = tu
        self.mau = mau
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    def rutGon(self):
        ps = PhanSo()
        ucln = math.gcd(self.tu,self.mau)
        ps.tu = self.tu/ucln
        ps.mau = self.mau/ucln
        return ps
    def __add__(self, other):
        ps = PhanSo()
        ps.tu = self.tu * other.mau + other.tu * self.mau
        ps.mau = self.mau * other.mau
        return ps.rutGon()
    def __sub__(self,other):
        ps = PhanSo()
        ps.tu = self.tu * other.mau - other.tu * self.mau
        ps.mau = self.mau * other.mau
        return ps.rutGon()
    def __mul__(self,other):
        ps = PhanSo()
        ps.tu = self.tu * other.tu
        ps.mau = self.mau * other.mau
        return ps.rutGon()
    def __truediv__(self,other):
        ps = PhanSo()
        ps.tu = self.tu * other.mau
        ps.mau = self.mau * other.tu
        return ps.rutGon()
a = PhanSo()
print(a)
a.tu = 2
a.mau = 3
print(a)
b = PhanSo(3,5)
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")