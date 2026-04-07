import pandas as pd
import numpy as np

# a = [1,2,3,4,3,2,1]
# myvar = pd.Series(a)
# print(myvar)

# myvar = pd.Series(a, index = ["a", "b", "c", "d", "c", "b", "a"])
# print(myvar)

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

# series01 = pd.Series(np.arange(2,8))
# print(series01)

# series02 = pd.Series(np.linspace(0,10,5))
# print(series02)
# print(series02.size)
# print(len(series02))
# print(series02.values)



# mydataset = {
#     "cars": ["BMW", "Honda", "Acura"],
#     "year": [2013, 2017, 2022]
# }

# myvar = pd.DataFrame(mydataset)
# print(myvar)

# myvar = pd.DataFrame(np.arange(1,8))
# print(myvar)
# print()
# df = pd.DataFrame(
#     [[1,2],
#      [3,4],
#      [5,6]]
# )
# print(df)

#second part of the lesson

# data = {
#     "calories": [520, 480, 400],
#     "duration": [50, 48, 40]
# }

# myvar = pd.DataFrame(data)
# print(myvar)
# print()
# index = ["day1", "day2", "day3"]
# myvar = pd.DataFrame(data, index)
# print(myvar)




# data = {
#     "Duration":{"0":60, "1":60, "2":60, "3":45, "4":45, "5":60},
#     "Pulse":{"0":110, "1":117, "2":103, "3":109, "4":117, "5":102},
#     "Maxpulse":{"0":130, "1":145, "2":135, "3":175, "4":148, "5":127},
#     "Calories":{"0":409, "1":479, "2":340, "3":282, "4":406, "5":300}
# }

# df = pd.DataFrame(data)

# print(df[ ['Duration', 'Calories'] ].head())

# print(df.loc['1'].head())
# print(df.loc['2'].head())



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"
    
#     def myFunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myFunc()
# print(p1)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x, self.y}"
    
    def get_location(self):
        return f"x: {self.x}\ny: {self.y}"
    
    def move_x(self, a):
        print(f"Adding {a} to x: {self.x}")
        return f"{self.x + a, self.y}"
    
    def move_x(self, a):
        print(f"Adding {a} to y: {self.y}")
        return f"{self.x, self.y + a}"
    
p1 = Point(2, 3)
p2 = Point(5, 6)

print(p1)
print(p2)