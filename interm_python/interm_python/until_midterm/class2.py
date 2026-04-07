#ids

#1
# def foo(arg):
#     print(id(arg), arg)


# def bar(arg):
#     print(id(arg), arg)
#     arg = 2
#     print(id(arg), arg)


# a = 0
# print(id(a), a)
# foo(a)
# bar(a)
# print(id(a), a)

#2
# class Door:
#     def __init__(self, number, status="closed"):
#         self.__number = number
#         self.status = status

#     def open(self):
#         self.status = "opened"

# l = [1, "string"]
# print(l)
# idl = id(l)
# l.append(Door(0))
# print(id(l) == idl)

# print(l)

# for e in l:
#     print(e)


#types

#1
# b: int = 2
# a = "a string"
# b = "b string"
# a = 1

#2
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} {self.age}"

#     def myFunc(self):
#         print(f"Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myFunc()
# print(p1)


#iterating lists 

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1


def doit(lst):
    for i in range(len(lst)):
        print(i)
        if i % 2 == 0:
            print(lst[i], end="\n")
            print("i before", i)
            i = i - 1
            print("i after", i)
        elif i == 7:
            print("exiting")
            break


thislist = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "olive",
    "milk",
    "cheese",
    "ananas",
    "avocat",
]
doit(thislist)
