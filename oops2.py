#del keyword

# class Student:
#     def __init__(self, name):
#         self.name = name 
        
# s1 = Student("PRABHA")
# print(s1.name)
# del s1.name 
# print(s1.name)

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass 

acc1 = Account("12345", "avnturk")
print(acc1.acc_no)
# print(acc1.__acc_pass) -> private = __


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass 
    def reset_pass(self):
        print(self.__acc_pass)
acc1 = Account("12345", "avnturk")
print(acc1.reset_pass)


class Person: 
    __name  = "anonymous"
    
    def __hello(self):
        print("hello person!!")
        
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())

# inheritance -> single level
# class Car:
#     color = "Black"
#     @staticmethod 
#     def start():
#         print("car started..")
#     @staticmethod 
#     def stop():
#         print("car stopped...")

# class BMWCar(Car):
#     def __init__(self, name):
#         self.name = name 
# car1 = BMWCar("M5")
# car2 = BMWCar("M7")
# print(car1.start())
# print(car2.stop())
# print(car1.color)


# multi-level 
# class Car:
#     @staticmethod 
#     def start():
#         print("car started..")
#     @staticmethod 
#     def stop():
#         print("car stopped...")

# class BMWCar(Car):
#     def __init__(self, brand):
#         self.name = brand

# class M5(BMWCar):
#     def __init__(self, type):
#        self.type = type 
# car1 = M5("disel")
# car1.start()


# multiple inheritance 
# class A: 
#     varA = "welcome to class A"
# class B:
#     varB = "welcome to class B"
# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA) 

# super class 
# class Car:
#     def __init__(self, type): 
#         self.type = type 
#     @staticmethod 
#     def start():
#         print("car started..") 
#     @staticmethod 
#     def stop():
#         print("car stopped..")
# class ToyotaCar(Car): 
#     def __init__(self, name, type): 
#         self.name = name 
#         # self.type = type -> shortcut using super class = super().__init__(type)
#         super().__init__(type)
#         super().start()
# car1 = ToyotaCar("prius", "electric")
# print(car1.type)    

# class method 
class Person:
    name = "anonymous"
    
    def changeName(self, name):
        self.name = name 
p1 = Person()
p1.changeName("rahul kumar") 
print(p1.name)
print(Person.name)