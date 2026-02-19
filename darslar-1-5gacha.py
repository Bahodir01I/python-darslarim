# # -*- coding: utf-8 -*-
# """
# Created on Sun Dec  7 21:24:44 2025

# @author: Bahodir
# """

# #4- dars o'zgaruvchilar

# #ism = "Bahodir"
# #yosh = 24
# #print(ism)
# #print(yosh)


# #ism = "Bahodir"
# #print(ism)
# #ism = "Bositxon"
# #print(ism)

# a = 6
# b = 8
# c = (a + b)**2
# #print(c)

# ism_familiya = 'Bahodir Ismoilov'

# s = "Hello world"
# #print(s)

# xabar = 'salom men bugun yangi narsalarni orggandim'
# #print(xabar)
# xabar= 'rostan?'
# #print(xabar)

# radius = 5
# pi = 3.14159
# aylana_yuzi= pi * radius
# #print("Radiusi", radius, "ga teng aylaning yuzi", aylana_yuzi) 



                        # # 6 - dars  String (Matn degani)

# #ism = " Bahodir"
# #smayli = "😃"
# #print(smayli)


# #ism = 'Bahodir'
# #print("Mening ismim " + ism)


# ism = 'Bahodir'
# familya = ' Ismoilov'
# #print(ism + familya)
# ism_sharif = f"{ism} {familya}"
# #print(ism_sharif)


# a_ism = "James"
# b_familya = "Bond"
# #print(f"Salom, mening ismim {b_familya}. {a_ism} {b_familya}!")


# #print("Hello world")
# #print("Hello \tworld")
# #print("Hello \nworld")




# ####  STRING METODLARI

# ism = 'Bahodir'
# familya = ' Ismoilov'
# ism_sharif = f"{ism} {familya}"
# #print(ism_sharif.upper())
# #print(ism_sharif.lower())
# #print(ism_sharif.title())
# #print(ism_sharif.capitalize())


meva = "   olma   "
print(meva)
print("Men" + meva.lstrip() + "yaxhi ko'raman")
print("Men" + meva.rstrip() + " yaxshi ko'raman")
print("Men" + meva.strip() + " yaxshi ko'raman")



# #####   INPUT         AMALIYOT


# Quyidagi mashqlarni bajaring:

# Quyidagi o'zgaruvchilarni yarating:
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.


# #ism = input("Ismingiz nima? \n")
# #print("Assalomu aleykum " + ism.title())

# #kocha = "Bog'bon"
# #mahalla = "sog'bon"
# #tuman = "Bodomzor"
# #viloyat = "Samarqand"

# #print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# print("Iltimos quyidagi ma'lumotlaringizni kiriting: ")
# kocha = input("Ko'changiz nomini kiriting? ")
# mahalla = input("Mahallangiz nomini: ")
# tuman = input("Tumaningizni kiriting endi: ")
# viloyat = input("Va viloyatingizni ham, iltimos: ")


# #print(kocha + " ko'chasi " + mahalla + " mahallasi " + tuman + "t umani " + viloyat + " viloyati")
# #print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + tuman + "tumani,\n" + viloyat + " viloyati")
# manzil = (f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
# print(manzil)
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())
# print(manzil.title())






####                        6-dars:   sonlar bilan ishlash


# a = 20
# b = 5.5
#c = a + b
#temp = 36.6
#print(c)
#print(type(a))


# aholi_soni = 6_852_758_125
#print("Aholi soni: ", aholi_soni)


# x, y, z = 10, 6.6, -66

# c = a*b

# d = 100//2



# radius = 20
# PI = 3.14159
# diametr = 2 * radius
# print("Aylananing uzunligi=", PI*diametr)


# ism = "Jonir"
# yosh = 24
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)

# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2025 - t_yil
# print("Siz", yosh, " yoshda ekansiz")

# a = int("20")
# b = float("30")
# temp = str(36.6)


#                                    Amaliy mashqlar


# AMALIYOT
# Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur




# 1 - topshiriq

# a = int(input("Istalgan sonni kiriting: "))
# b = a ** 2
# c = a ** 3
# print(str(a) + " ning kvadrait ", b, " ga teng")
# print(str(a) + " ning kubi ", c, " ga teng")


# 2 - topshiriq

# a = int(input("Iltimos yoshingizni kiriting: "))
# t_yill = 2025 - a
# print("Siz", t_yill, "- yilsiz")


# 3 - topshiriq

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# yig = a + b
# ayir = a - b
# kop = a * b
# bol = a / b
# # print(a)
# print('yigindi', yig, ' ga teng\n', 'ayirmasi', ayir, "ga teng\n", "ko'paytmasi", kop, "ga teng\n", "bo'linmasi", bol, "ga teng" )




###                     7 - dars:   LIST

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narxlar = [12000, 18000, 10900, 22000, 360000, -26, 63.23]
# sonlar = ['bir', 'uch', 1521, 525, 6]
# ismlar = []


# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']

# bozorlik = ['yo\'g', 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yhatdan mahsulotni sug'urib olish
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)


#                   Amaliy mashqlar

# 1 - topshiriq

# ismlar = ['Olloyor', 'Yusufali', 'Jamshid']
# print(ismlar)
# print(ismlar[0] + " qachon kelasan uyga?")
# print("Assalomu aleykum toy nimaga, qachon endi " + ismlar[1])
# print("To'y qachon endi " + ismlar[2])

# 2 - topshiriq

# sonlar = [12520, 55222, 23, -23, 63.3, 66]
# sonlar[0] = sonlar[0] + 20000
# print(sonlar)
# sonlar.insert(2, 50000)
# print(sonlar)
# del sonlar[3]
# print(sonlar)


# 3 -topshiriq

# t_shaxslar = ["Alisher Navoiy", "Bobur", 'Amir Temur']
# z_shaxslar = ["Abror Muxtor Ali", "Umidjon Eshmuhammedov", 'Muhammad Ali Eshonqulov']
# print(t_shaxslar)
# print(z_shaxslar)
# print("Men tarixiy shaxslardan " + t_shaxslar.pop(1) + " bilan va zamonaviy shaxslardan esa " + z_shaxslar.pop(2) + " bilan ko'rishishni istardim")


# 4 -topshiriq

# friends = []
# # friends = friends.append("Olloyor")
# # print(friends)
# friends.append('Behruz')
# friends.append('Abror')
# friends.append('Jamshid')
# friends.append('Javohir')
# friends.append('Yusuf ali')
# friends.append('Olloyor')
# print(friends)
# friends.insert(0, "Bojalar")
# print(friends)
# friends.remove('Abror')
# print(friends)
# friends.insert(5, 'Tohir')
# print(friends)


# mehmonlar = []
# print(mehmonlar)
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(0))
# print(mehmonlar)





