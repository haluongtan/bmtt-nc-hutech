def chiaHetCho5(soNhiPhan):
    soThapPhan = input(soNhiPhan, 2)
    if soThapPhan %5==0:
        return True
    else:
        return False
chuoiSoNhiPhan = input("Nhap chuoi so nhi phan (Phan tach boi dau phay): ")
soNhiPhanList = chuoiSoNhiPhan.split(',')
soChiaHetCho5 = [so for so in soNhiPhanList if chiaHetCho5 (so)]
if len(soChiaHetCho5) > 0:
    ketQua = ','.join(soChiaHetCho5)
    print("Cac so nhi phan chia het cho 5 la:",ketQua)
else:
    print("Khong co so nhi phan nao chia het cho 5 trong chuoi da nhap.")
    