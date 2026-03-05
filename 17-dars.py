# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 18:22:46 2025

17 - dars: INPUT() va While Tsikli

@author: Bahodir
"""


# ism = input("Iltimos ismingizni kiriting: ")
# savol = f"Salom {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = input(yosh)
# height = input("Bo'yingiz necha mert? ")
# height = float(height)



# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son +=1


# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dastur tohtashi uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat) ** 2)
# print("Dastur tugadi")





# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dastur tohtashi uchun 'exit' deb yozing): "

# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)
# print("Dastur to'xtadi")




# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dastur tohtashi uchun 'exit' deb yozing): "

# while True:
#     qiymat  = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat) ** 2)
        
# print("Dastur to'xtadi!")



# sonlar  = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f"{son} ning kvadrati {son ** 2} ga teng!")
# print("Dastur tugadi!!")


# sonlar  = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son ** 2} ga teng!")


# son = 0
# while son < 10:
#     son += 1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)


# son = 0
# while son < 10:
#     son += 1
#     if son%2 ==0:
#         continue
#     else:
#         print(son)



# son = 0
# while son < 10:
#     son += 1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)



#                         Amaliyot 

# 1 - mashq

# savol = "Iltimos yoqtirgan kitobingizni kiriting: "
# savol += " (Agar barchasini kiritgan bo'lsangiz to'xtash uchun 'exit' deb yozing.) "

# while True:    
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print("Raxmat! ")



# 2 - mashq

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         print("Raxmat!")
#         break 
#     yosh = int(qiymat)
    
#     if yosh <7:
#         narh = 2000
#     elif 7<yosh<18:
#         narh = 3000
#     elif 18<yosh<65:
#         narh = 10000
#     else:
#         narh = 0
        
#     if narh ==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta narxi {narh}")



# 3 - mashq

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")



#  18 -dars  WHILE VA RO'YXATLAR


# print("Yaqin do'stlaringizni ismini kiriting: ")
# n = 1
# ismlar = []
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana qo'shasizmi? (ha/yo'q) ")
#     n +=1
#     if takrorlash != 'ha':
#         break
   

# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())



# print("Do'stlarni yoshini saqlaymiz ")
# dostlar = {}
# ishora = True


# while ishora:
#     ism = input("Do'stinigizni ismini kiriting: ")
#     yosh = input(f"{ism.title()} - ning yoshini kirting: ")
#     dostlar[ism] = int(yosh)
    
#     savol = input("Yana boshqa ism kiritasizmi? (ha/yo'q) ")
#     if savol == "yo'q":
#         ishora = False
    
# print("Do'stlaringiz ma'lumotlari: ")
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} - ning yoshi {yosh} ")



# cars = ["lacetti", 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia', 'lacetti']
# while 'nexia' in cars:
#     cars.remove('nexia')

# print(cars)



# talabalar = ['hasan', 'husan', 'olim', 'bobur']
# baholangan_talabalar = {}

# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()} - ning bahosini kiriting: ")
#     print(f"{talaba.title()} bahonlandi.")
#     baholangan_talabalar[talaba] = int(baho)


#                       AMALIYOT            

# 1 - mashq

# buyurtma = []

# while True:
#     zakas = input("Iltimos buyurtmaningizni kiriting: ")
#     buyurtma.append(zakas)
#     yana = input("Yana nimadur qo'shasizmi? (ha/yo'q) ")
#     if yana == "yo'q":
#         break
# print(buyurtma)


# 2 - mashq

# print("e-bozor tovarlarini shakllantiradigan ro'yhat")
# mahsulotlar = {}
# ishora = True
    
# while ishora:
#     mahsulot = input("Iltimos mahsulot nomini kiriting? ")
#     print(f"{mahsulot.title()} saqlandi")
#     narx = input(f"{mahsulot.title()} ning narxini kiriting: ")
#     mahsulotlar[mahsulot] = int(narx)

#     yana = input("Yana mahsulot kiritasizmi? (ha/yo'q) ")
#     if yana == "yo'q":
#         ishora = False
        
# for mahsulot, narx in mahsulotlar.items():
#     print(f"Siz kiritingan {mahsulot.title()}ingiz va uning narhi -{narx}")



# 3 - mashq

# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narx = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narx} so'm")
#     else:
#         print(f"Bizda bunday {buyurtma} yo'q")
































