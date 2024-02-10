# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
#
#     def about(self):
#         print("I am GrandParent")
#
#     def about_myself(self):
#         print("I am GrandParent")
#
#
# class Parent(Grandparent):
#     age = 33
#
#     def about_myself(self):
#         print("I am Parent")
#
#
# class Child(Parent):
#     height = 50
#     age = 2
#     super().about()
#     super().about_myself()
#
#     def __init__(self):
#         print(self.age)
#         print(self.height)
#         print(self.satiety)


# class Class1:
#     var = 10
#
#     def __init__(self):
#         self.var = 20
#
#
# class Class2(Class1):
#     def __init__(self):
#         print(self)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
#
# cl = Class2


# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#
#         def printer(self):
#             print(self.hello)
#             print(self._hello)
#             print(self.__hello)
#             print(self.world)
#             print(self._world)
#             print(self.__world)
#
#
# class Hi(Hello_world):
#     def hi_printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
# hello = Hello_world()
# hello.printer()
# hi = Hi()
# hi.hi_printer()
# ch = Child()


class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128


class Monitor:
    def __init__(self):
        self.resolution = "4K"


class SmartPhone(Computer, Monitor):
    def print_info(self):
        print(self.memory)
        print(self.resolution)


iphone = SmartPhone()
iphone.print_info()
