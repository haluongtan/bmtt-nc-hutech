soGioLam = float(input("Nhap so gio lam moi tuan: "))
luongGio = float(input("Nhap thu lao tren moi gio lam tieeu chuan: "))
gioTieuChuan = 44
gioVuotChuan = max(0, soGioLam - gioTieuChuan)
thucLinh = gioTieuChuan * luongGio + gioVuotChuan * luongGio * 1.5
print(f"So tien thuc linh cua nhan vien: {thucLinh}")
