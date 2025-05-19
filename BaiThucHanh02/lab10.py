def daoNguocChuoi(chuoi):
    return chuoi[::-1]
input_string = input("Moi nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la: ",daoNguocChuoi(input_string))