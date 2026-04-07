# lambda functions
# x = lambda a : a + 10
# print(x(5))

# y = lambda a, b : a * b
# print(y(5, 6))

# z = lambda a, b, c : a + b + c
# print(z(5, 6, 2))

# square = lambda x : x ** 2
# print(square(5))


# classess

class Door:
    def __init__(self, number, status="closed"):
        self.__number = number
        self.status = status

    def open(self):
        self.status = "opened"

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number
    
    def __repr__(self):
        return f"<Door: number {self.__number} status {self.status}>"
    
    def __str__(self):
        return f"From str method of Door: number is {self.__number} status is {self.status}"
    
# l = [1, "string"]
# print(l)
# idl = id(l)
# l.append(Door(0))
# print(id(l) == idl)
# print(l) #list are mutable. even after .append the id doesn't change

# __repr__ vs __str__
# a = 42
# print(repr(a), type(repr(a)))

# s = "Hello \n chat"
# print(repr(s), type(repr(s)))

# l = [1,2,3]
# print(repr(l), type(repr(l)))

# st = {1,2,3}
# print(repr(st), type(repr(st)))

# print(str(s))

# Back to types
# from collections.abc import Sequence
# from typing import TypeVar

# T = TypeVar("T")


# def firstT(seq: Sequence[T]) -> T:
#     return seq[0]

# #VS

# def first(seq):
#     return seq[0]

# def sqrint(x: int) -> int:
#     return x * x

# #VS

# def sqr(x):
#     return x * x

# b: int = 2.5
# print(b)
# print(type(b))

# c: int = 2
# print(c)
# print(type(c))

# #VS

# f = 3
# print(f)
# print(type(f))

# d = (4.0, 1, 2)
# print(firstT(d))
# print(type(firstT(d)))

# print(first(d))
# print(type(first(d)))

# e: str = 5
# print(e)
# print(type(e))

# g: str = "7"
# print(g)
# print(type(g))

# def doit(i: int):
#     print("int", i)

# def doit(s: str):
#     print("str", s)

# def doit(f: float):
#     print("float", f)

# doit(0)
# doit("0")
# doit(1.1)

def fact(n):
    if n in [0,1]:
        return 1
    return fact(n-1) * n

num = 7
print(fact(num))

inp = int(input("Pls enter a number: "))
print(fact(inp))