def taoTuplrTuList(lst):
    return tuple(lst)
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
myTuple = taoTuplrTuList(numbers)
print("List: ",numbers)
print("Tuple tu List: ",myTuple)