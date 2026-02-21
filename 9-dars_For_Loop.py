"""
Created on Wed Dec 17 09:39:00 2025

#9-dars FOR LOOP

"""

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     # print("Salom", mehmon)
#     # print("Xayr, ", mehmon)
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nohorga oshga taklif etamiz")
#     print("Hurmat bilan,  Mamadaliyevlar oilasi\n")


# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")




# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlar_kvadrati)

#
# dostlar = []
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-dostingizni ismini kiriting:"))
# print(dostlar)



#  AMALIYOTLAR

# 1 - mashq

# ismlar = ['ali', 'bobur', 'jamshid', 'islom', 'olim']
# for i in ismlar:
#     print(f"Assalomu aleykum do'stim {i}")
# print(len(ismlar), "marta kod takrorlandi")


# toq_sonlar = list(range(11, 100, 2))
# for son in toq_sonlar:
#     print(f"{son}-ning kubi {son**3} ga teng:")


# kinolar = []
# print("Eng simivli 5 ta kinoingizni nomini kiriting: ")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1}-yoqtirgan kinoyim: "))
# print(kinolar)


# n_suhbatlashgan = int(input("Bugun nechta odam bilan suhbatlashdingiz? "))
# ismlar = []
# for n in range(n_suhbatlashgan):
#     ismlar.append(input(f"{n+1}-chi suhbat qilgan odaminkiz kim bo'lgan?"))
# print(ismlar)



#              10 - dars  TARMOQLANISH


# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == "bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())
        
  
# ism = 'Ali'
# ism.lower() == 'ali'


# ism = input("Ismingiz nima? \n >>>")
# if ism.lower() != 'ali':
#     print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
# else:
#     print("Salom, Ali")
        

# javob = float(input("12*6 nechiga teng?>>>"))
# if javob !=72:
#     print("Javob xato!")


# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18:
#     print("Xush kelibsiz!")
# else:
#     print("Kirish mumkin emas!")
            
        
# login = input("Yangi loginni tanlang:")
# if len(login)<=5:
#     print("Login 5 harfdan ko'proq bo'lishi shart!")        


# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2020-yil<18:
#     print(f"Yoshingiz {2020-yil} da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")        


# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")        


# x, y = 250, 50
# print("x>y") if x>y else print("x<y")        
        

#   AMALIYOT

# 1 - mashq

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']    
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else: 
#         print(car.title())


# 2 - mashq

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']    
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else: 
#         print(car.upper())        


# 3 - mashq

# login = input("Iltimos login ismni kiriting: ")
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin!\nFoydalanuvchilar ro'yhatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login.title()}")


# 4 - mashq

# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print("sonlar teng")
# else:
#     print("sonlar teng emas")


# 5 - mashq
# son = int(input("Istalgan sonni kiriting: "))
# if son >=0:
#     print("Bu musbat son")
# else:
#     print("Bu manfiy son")        


# 6 - mashq

# son = int(input("Iltimos ixtiyoriy sonni kiriting: "))
# if son > 0:
#     print(son**(1/2))
# else:
#     print("Iltimos musbat sonni kiriting")        
        
        
        
        
#              11 - dars  if-elif-else


# son = -60
# if son < 0:
#     print("son manfiy")
# else:
#     print("Son musbat")


# yosh = int(input("Yoshingizni kiriting? "))
# if yosh <= 4:
#     print("Sizga kirish bepul")        
# elif yosh <=12:
#     print("Sizga kirish narxi 4 ming so'm")
# elif yosh <=18:
#     print("Sizga kirish narxi 6 ming so'm")    
# else: 
#     print("Sizga kirish 10 ming sum")



# kun = input("Bugun nima kun? >>> ")
# if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni")        



# kun = input("Bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday? "))

# if kun.lower()=="yakshanba" and harorat>=30:
#     print("Cho'milgani boramizmi?")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")




# kun = input("Bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday? "))

# if (kun.lower()=="yakshanba" or kun.lower()=="shanba") and harorat>=30:
#     print("Cho'milgani boramizmi?")
# elif (kun.lower()=="yakshanba" or kun.lower()=="Shanba") and harorat<=30:
#     print("Uyda dam olamiz!")


# narh = 15000
# choy = True
# salat = True

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
# print(f"Jami {narh} so'm")



# narh = 15000
# choy = True   #   bu True va False ni o'rniga 1 yoki 0 ishlatska ham bo'ladi
# salat = False
# non = True
# kompot = True
# assosrti = False

# if choy:
#     print('Mijoz choy oldi')
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assosrti:
#     print("Mijoz assorti oldi")
#     narh = narh + 15000
# print(f"Jami {narh} so'm")    

        

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']  
# # 'mani' in menu      
        
# ovqat = input("Siz nima ovqat yeysiz? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")
        
  
        
# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']  
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']  


# taom in buyurtmalar
#   if taom in menu:
#       print(f"Menyuda {taom} bor")
 #   else:
  #      print(f"Kechirasiz, menyuda {taom} yo'q")



#            AMALIYOT UCHUN MASHQLAR

# 1 mashq
# son = int(input("Iltimos juft son kiriting: "))
# if son % 2 == 0:
#     print("Raxmat!")
# else:
#     print("Bu son juft emas")


# 2 mashq
# yosh = int(input("Iltimos yoshingizni kiriting: "))
# if yosh < 4 or yosh > 60:
#     print("Siz uchun bepul")
# elif yosh < 18:
#     print("Siz uchun 10 ming so'm")
# elif yosh > 18:
#     print("siz uchun 20 ming so'm")

# 3 -mashq

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for mahsulot in range(5):
#     savat.append(input(f"Iltimos {mahsulot+1} - mahsulotni kiriting:"))
    
# for n in savat:
#     if n in mahsulotlar:
#         print(f"Do'konimizda {n} bor")
#     else:
#         print(f"Do'konimizda {n} yo'q")


# 4 - mashq

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for mahsulot in range(5):
#     savat.append(input(f"Iltimos {mahsulot+1} - mahsulotni kiriting:"))
    
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in savat:
#     if n in mahsulotlar:
#         bor_mahsulotlar.append(n)
#     else:
#         mavjud_emas.append(n)
        
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulot yo'q: ")
#     for n in mavjud_emas:
#         print(n)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


# 5 - mashq

# foydalanuvchilar = ['olloyor', 'bobur', 'nodir', 'qodir', 'sobir']

# login = input("Yangi loginni kiriting: ")
# if login in foydalanuvchilar:
#     print("Login band, boshqa login tanlang!")
# else:
#     print("Xush kelibsiz, foydalanuvchi!")



#  6 -mashq
# n = int(input("Iltimos bironta butun sonni kiriting:"))
# for i in range(2, 11):
#     if not (n%i):
#         print(f"{n} soni {i} ga qoldiqsiz bo'linadi")
    





        