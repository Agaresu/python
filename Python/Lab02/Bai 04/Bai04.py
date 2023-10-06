class PhanSo:
    def __init__(self, tu = 1, mau = 1) -> None:
        self.tu = tu
        self.mau = mau
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
class DSPhanSo:
    f = open("Bai 04/duLieu.txt","r")
    print(f.read())
    def timSoAm(self):
        for i in self.f:
            if self.tu * self.mau < 0:
                i += 1
                return i
DSPhanSo.timSoAm