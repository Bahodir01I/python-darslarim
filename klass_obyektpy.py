"""
Created on Mon Jan 26 19:25:15 2026

#       Klass va Obyekt

@author: Bahodir
"""


matn = "Assalomu aleykum"

class Kompyuter:
    def __init__(self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu
        
        
    def info(self):
        inf = f"{self.model}, RAM:{self.ram}, SSD:{self.hdd}, CPU:{self.cpu} "
        return inf
        
        
macbook = Kompyuter("Apple Macbook", "8GB", "512GB", "M1", "M1")
print(macbook.info())




# import pickle
#
# with open('info', 'rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
#
# print(talaba1)
# print(talaba2)