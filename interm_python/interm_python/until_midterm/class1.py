'''
num = int(input())
lines = ["*" * i for i in range(1, num * 2 + 1, 2)]

max_line = max(lines, key=len)
for el in lines:
    spacing = (len(max_line) - len(el)) // 2
    print(" " * spacing + el + " " * spacing)
'''
#teacher's code

rows = 10
k = 2 * rows + 1
for i in range(rows):
    for j in range(0, 2*k + 1):
        print(end = " ")
    k = k - 1
    for j in range(0, 2*i + 1):
        print("*", end = " ")
    print("")

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(lst)):
#     if i % 2 == 0:
#         print(lst[i], end="\n")
#         i = i - 1
#     elif i == 7:
#         break


# i think we can turn any iterable into tuple, list, set or dict using built-in classes
# but we can define them explicitly too
# from collections.abc import Sequence
# from typing import TypeVar

# T = TypeVar("T")


# def first(seq: Sequence[T]) -> T:
#     return seq[0]


# my_list = [1, 2, 3]
# print(type(my_list))
# print(first(my_list))

# my_tuple = (1, 2, 3)
# print(type(my_tuple))
# print(first(my_tuple))

# my_set = {1, 2, 3}
# print(type(my_set))


# my_dict = {"first": 1, "second": 2, "third": 3}
# print(type(my_dict))
