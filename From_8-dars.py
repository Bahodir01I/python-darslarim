

"""
Created on Wed Dec 10 15:55:17 2025

Dasturlash asoslari
08-dars: LISTS

@author: Bahodir
"""



# cars = ['bmw', 'mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']

# narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Enga arzon narx", arzon, "Eng qimmati", qimmat )


# cars = ['bmw', 'mercedes benz', 'vovlo', 'gm', 'tesla', 'audi']






# #Consoleda yozganlarim
# cars
# Out[30]: ['bmw', 'mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']

# cars.reverse()

# cars
# Out[32]: ['audi', 'tesla', 'general motors', 'vovlo', 'mercedes benz', 'bmw']

# len(cars)
# Out[33]: 6

# cars
# Out[34]: ['audi', 'tesla', 'general motors', 'vovlo', 'mercedes benz', 'bmw']

# len(sonlar)
# Out[35]: 8

# sonlar
# Out[36]: [998, 56, 45, 23, 12, 1, -5, -7.2]

# uzunlik = len(sonlar)

# sonlar = list(range(0, 10))

# list(range(21, 30))
# Out[39]: [21, 22, 23, 24, 25, 26, 27, 28, 29]

# list(range(21, 31))
# Out[40]: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# t_sonlar = list(range(1, 20, 2))

# t_sonlar
# Out[42]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# juft_sonlar = list(range(0, 20, 2))

# juft_sonlar
# Out[44]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# sanash = list(range(0, 101, 10))

# print(sanash)
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# t_sonlar
# Out[47]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# max_qiymat = max(t_sonlar)

# max_qiymat
# Out[49]: 19


# print(narxlar)
# [12000, 22500, 23456, 9800, 5600, 9934, 32874]

# min(narxlar)
# Out[52]: 5600

# max(narxlar)
# Out[53]: 32874

# sum(narxlar)
# Out[54]: 116164

# Enga arzon narx 5600 Eng qimmati 32874

# cars
# Out[56]: ['bmw', 'mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']

# print(cars[0])
# bmw

# print(cars[4])
# tesla


# print(cars[0:3])
# ['bmw', 'mercedes benz', 'vovlo']

# print(cars[2:6])
# ['vovlo', 'general motors', 'tesla', 'audi']

# cars
# Out[62]: ['bmw', 'mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']

# print(cars[:3])
# ['bmw', 'mercedes benz', 'vovlo']

# print(cars[1:])
# ['mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']

# cars
# Out[65]: ['bmw', 'mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']

# cars
# Out[66]: ['bmw', 'mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']

# my_cars = cars

# print(cars)
# ['bmw', 'mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']

# print(my_cars)
# ['bmw', 'mercedes benz', 'vovlo', 'general motors', 'tesla', 'audi']



# my_cars.remove('vovlo')

# print(my_cars)
# ['bmw', 'mercedes benz', 'general motors', 'tesla', 'audi']

# my_cars[0] = 'lacetti'

# print(my_cars)
# ['lacetti', 'mercedes benz', 'general motors', 'tesla', 'audi']

# print(cars)
# ['lacetti', 'mercedes benz', 'general motors', 'tesla', 'audi']

# cars
# Out[76]: ['lacetti', 'mercedes benz', 'general motors', 'tesla', 'audi']

# my_cars
# Out[77]: ['lacetti', 'mercedes benz', 'general motors', 'tesla', 'audi']

# cars.append('bmw')

# cars
# Out[79]: ['lacetti', 'mercedes benz', 'general motors', 'tesla', 'audi', 'bmw']

# my_cars
# Out[80]: ['lacetti', 'mercedes benz', 'general motors', 'tesla', 'audi', 'bmw']

# Enga arzon narx 5600 Eng qimmati 32874

# cars
# Out[82]: ['bmw', 'mercedes benz', 'vovlo', 'gm', 'tesla', 'audi']

# my_cars = cars[:]

# my_cars
# Out[84]: ['bmw', 'mercedes benz', 'vovlo', 'gm', 'tesla', 'audi']

# my_cars.remove('bmw')

# my_cars
# Out[86]: ['mercedes benz', 'vovlo', 'gm', 'tesla', 'audi']

# cars
# Out[87]: ['bmw', 'mercedes benz', 'vovlo', 'gm', 'tesla', 'audi']



#                        #Tuple

# toys
# Out[91]: ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

# toys[0]
# Out[92]: 'bus'

# toys[-1]
# Out[93]: 'lizard'

# toys[2:5]
# Out[94]: ('bear', 'dino', 'snake')

# toys[3:]
# Out[95]: ('dino', 'snake', 'lizard')

# toys[0] = "teddy"
# Traceback (most recent call last):

#   Cell In[96], line 1
#     toys[0] = "teddy"

# TypeError: 'tuple' object does not support item assignment


# toys
# Out[97]: ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

# toys.append("teddy")
# Traceback (most recent call last):

#   Cell In[98], line 1
#     toys.append("teddy")

# AttributeError: 'tuple' object has no attribute 'append'


# toys.remove('bear')
# Traceback (most recent call last):

#   Cell In[99], line 1
#     toys.remove('bear')

# AttributeError: 'tuple' object has no attribute 'remove'


# toys
# Out[100]: ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

# toys = list(toys)

# type(toys)
# Out[102]: list

# toys.append('teddy')

# toys
# Out[104]: ['bus', 'car', 'bear', 'dino', 'snake', 'lizard', 'teddy']

# toys = tuple(toys)

# type(toys)
# Out[106]: tuple


## TUPLE

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

#   Amaliyot

# 1 - mashq

# davlatlar = ['Uzbekistan', 'Korea', 'US', 'UK', 'Dubai', 'BAA']
#taomlar = ['osh', 'manti', 'shorva', 'kabob', 'qotirma']






