a=5
b=3
result=a+b
print("Ket qua:",result)


a=8
b=4
result=a-b
print("Ket qua:",result)


a=6
b=7
result=a*b
print("Ket qua:",result)


a=20
b=5
result=a/b
print("Ket qua:",result)


a=20
b=3
result=a//b
print("Ket qua:",result)


a=20
b=7
remaider=a%b
print("Ket qua:",remaider)

a=2
b=3
result=a**b
print("Ket qua:",result)


x=5
y=3
result = (x>2) and (y<4)
print("Ket qua:",result)


x=5
y=3
result=(x>2) or (y>4)
print("Ket qua:",result)


x=5
y=3
result = not (x==5)
print("Ket qua:",result)


x=5
result = (x==5)
print("Ket qua:",result)

x=5
result=(x!=3)
print("Ket qua:",result)


x=5
result1=(x>3)
result2=(x<3)
print("Ket qua:",result1, "Ket qua:",result2)



x=5
result1 = (x>=3)
result2=(x<=3)
print("Ket qua:",result1, "Ket qua:",result2)


name = input("Nhap ten cua ban:")
print("xin chao,",name)


age=21
print("Tuoi cua ban la:",age)

print("Python","la","ngon","ngu","lap","trinh", sep="-")
print("xin chao",end=" ")
print("cac ban!")


x=10
if x>5:
    print("x lon hon 5")
elif x==5:
    print("x bang 5")
else:
    print("x nho hon 5")


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


count = 0
while count <5:
    print(count)
    count+=1



for i in range(1, 101):
    if i%5 == 0:
        print("So chia het cho 5 dau tien la:",i)
        break



for i in range(1,11):
    if i%2!=0:
        continue
    print(i)



x=5
if x>10:
    print("x lon hon 10")
else:
    pass



string_single_quotes = 'Day la mot chuoi su dung dau ngoac don.'
string_double_quotes = "Day la mot chuoi su dung dau ngoac kep."
string_triple_quotes = '''Day la mot chuoi
su dung dau ngoac ba,
co the trai dai qua nhieu dong.'''


my_string = "Hello, World!"
print(my_string[0])
print(my_string[7])


my_string = "Hello, World!"
print(my_string[7:])
print(my_string[:5])
print(my_string[3:8])

string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)

my_string= "Hello, World!"
length = len(my_string)
print(length)

my_string = "   Hello, World!"
print(my_string.strip())

my_string = "Hello, World!"
print(my_string.split(","))

my_string = "Hello, World!"
print(my_string.replace("Hello","Hi"))


def my_function(parameter1, parameter2):
    result = parameter1 + parameter2
    return result
result = my_function(10, 20)
print(result)


def calculate_sum(a,b):
    result = a + b
    return result
sum_result = calculate_sum(10,20)
print("Tong hai so la:",sum_result)


def greet(name):
    print("Xin chao,", name)
greet("Tam")



# from array import array
# int_array = array('i', [1, 2, 3, 4, 5])
# float_array= array('f',[3.14, 2.5, 6.7])
# print(int_array[0])
# print(float_array[2])
# int_array[2] = 10
# int_array.append(6)
# float_array.remove(6.7)

#.................................................................

my_list = [1,2,3,4,5]
names = ["Alice","Bob","Charlie"]
mixed_list = [10,"hello",3.14,True]
print(my_list[0])
print(names[2])
my_list[1] = 20
print(my_list)
names.append("David")
print(names)
del my_list[2]
print(my_list)
for element in names:
    print(element)


my_tuple = (1,2,3,4,5)
names = ("Alice","Bob","Charlie")
mixed_tuple = (10,"hello",3.14)
print(my_tuple[0])
print(names[2])


my_tuple = (1,2,3,1,4,1)
print(my_tuple.count(1))


my_tuple = ('a','b','c','d','b')
print(my_tuple.index('b'))


my_dict = {}
person = {"name":"Alice","age": 25, "city":"New York"}
print(person["name"])
print(person["age"])
person["email"] = "alice@example.com"
person["age"] = 26
del person["city"]
age = person.pop("age")
print(person.keys())
print(person.values())
print(person.items())



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def get_info(self):
        return f"{self.brand} {self.model}"
my_car = Car("Toyota", "Corolla")
print(my_car.get_info())


class ClassName:
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def get_info(self):
        return f"{self.brand} {self.model}"
my_car = Car("Toyota", "Corolla")
print(my_car.get_info())


# class ClassName:
#     def __init__(self, attribute1, attribute2):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2
#     class_attribute = "Class Attribute"
# object_name = ClassName(value1, value2)
# print(object_name.attribute1)
# print(object_name.class_attribute)


# class ClassName:
#     def method_name(self, parameter1, parameter2):
#         return something
# object_name = ClassName()
# object_name.method_name(value1, value2)


class Caculation:
    def add(self, a, b):
        return a+b
    def add(self, a, b, c):
        return a+b+c


class Animal:
    def make_sound(self):
        return "Generic sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Animal:
    def make_sound(self):
        return "Generic sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
def animal_sound(animal):
    return animal.make_sound()
dog = Dog()
cat = Cat()
print(animal_sound(dog))
print(animal_sound(cat))


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())