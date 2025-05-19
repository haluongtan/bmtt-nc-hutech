def tinhTongSoChan(list):
    tong =0
    for num in list:
        if num % 2 ==0:
            tong+=num
    return tong
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
tongChan = tinhTongSoChan(numbers)
print("Tong cac so chan trong list la:", tongChan)