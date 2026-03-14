
"""
Created on Mon Jan 26 00:34:44 2026

#24 - dars MODULLAR

@author: Bahodir
"""


import math

x = 400
print(math.sqrt(x))
print(math.pow(6, 4))
print(math.pi)
print(math.log2(8))
print(math.log10(100))








import random as r


#randin() bu randomli sonni tanlaydi

son = r.randint(0, 100)
print(son)


# choice() bu ham shu berilgan  royxatdagi ixtiyoriy qiymatlar yani harflar, sozlar, sonlar va hokazo ichidan tanlaydi

ismlar = ['olim', 'bahodir', 'hasan', 'husan']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))


x = list(range(0, 66, 4))
print(x)
print(r.choice(x))



# shuffle()  bu shuffle aralashtirib tashlaydi

x = list(range(14))
print(x)
r.shuffle(x)
print(x)









"""
Created on Mon Jan 26 00:34:44 2026

#24 - dars FUNKSIYALAR SO'NGSO'Z

@author: Bahodir
"""



import math


def nom(argument):
    return ifoda

# lambda argument1, argument2:ifoda=argument1+argument2


uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi, 10))


kvadrat = lambda x, y : x ** y
print(kvadrat(4, 2))


def daraja(n):
    return lambda x : x ** n

kvadrat = daraja(2)
kub = daraja(3)
w = daraja(4)
print(f"3 - ning kvadrati {kvadrat(3)} ga, "
      f"kubi {kub(3)} ga teng")













from math import sqrt # sqrt kvadrat ildiz


sonlar = list(range(11)) # bu 0, 10 gacha bo'lgan sonlarni shakllantirib olamiz
ildizlar = list(map(sqrt, sonlar))
print(sonlar)
print(ildizlar)



def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x * x


print(list(map(daraja2, sonlar)))



kvadratlar = list(map(lambda x : x * x, sonlar))


kvadratlar = []   # bu oddiy usuli yani lambda nomsiz funksiya va map funksiyani ishlatmasak shunday yozishimiz kerak
for son in sonlar:
    kvadratlar.append(son * son)
print(kvadratlar)



a = [4, 6, 8]
b = [9, 7, 6]

a_plus_b = list(map(lambda x, y: x+ y, a, b))
print(a_plus_b)












import random as r


sonlar = r.sample(range(100), 12) # 0 - 99 sonlar oralig'ida randomly 12 sonni tanlaydi
print(sonlar)
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaradi"""
    return x%2==0

juft_sonlar = list(filter(juftmi, sonlar))
print(juft_sonlar)

juft_sonlar = list(filter(lambda x : x%2==0, sonlar))
print(juft_sonlar)



mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", "banan"]
harf = 'o'
mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
print(mevalar)


mevalar2 = list(filter(lambda meva: len(meva)<=4, mevalar))
print(mevalar2)

mevalar2 = list(filter(lambda meva : (meva.startswith('a') and meva.endswith('r')), mevalar))





"""
Created on Mon Jan 29 00:34:44 2026

# Xatolar bilan ishlash

@author: Bahodir
"""



# SintaxError - bu qoidalarga amal qilmasdan kod yozish tushuniladi

print ("Hello world")
print("Hello world!")


print("Hello world!")


# IndentationError - bu kodni surib yozish degani

print("O'ngacha sanaymiz!")
for i in range(10):
    print(i+1)




# Bu run time error bu faqat dastur bajarilganda kelib chiqadi


# TypeError  - bu malumot bir malumot turi ustida bajarib bo'lmaydigan amalni bajarmoqchi bo'lgan chiqadi 

son = input("Istalgan sonni kiriting: ")
son = int(son)
print(f"{son} ning kvadrati {son**2} ga teng")


# NameError - bu malum bir o'zgaruvchi yoki funksiyani nomini xato yozib qo'yish natijasida chiqiqb keladi

# prit("Hello world!")
# mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
# for meva in mvalar:
#     print(meva)


# ValueError - bu noto'g'ri qiymat berib qo'yilgan chiqadi

son = float(input("Istalgan sonni kiriting: "))
if son >= 0:
    print("Musbat son")
else:
    print("Manfiy son")


#  #IndexError - bu malu'm bir ro'yhatni ichidagi qiymatlarga noto'g'ri index bilan murojat qilish

mevalar = ['olma', 'anor', 'uzum']
print(mevalar[3])


# ZeroDivisionError - bu degani 0 bo'lish xatoligi

x, y = 60, 50
z = 250/(x-y)




#  Mantiqiy xatolar - bu dastur yozish jarayonida o'zimiz yo'l qo'ygan xatolar

radius = 6
pi = 4.14
aylana_yuzi = pi * radius ** 2
print(aylana_yuzi)



son = float(input("Istalgan sonni kiriting: "))
ildiz = son ** (1/2)
print(f"{son} ning ildizi {ildiz} ga teng")


mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
for meva in mevalar:
    print(meva)
print("Dastur tugadi")


#       AMALIYOT


son = float(input("Juft son kiriting: "))
if son%2==0:
    print("Bu son juft son.")
else:
    print("Bu son juft emas.!")





yosh = int(input("Yoshingiz nechida? "))

if yosh<=4 or yosh>=60:
    narh = 0
    print(f"Chipta {narh} so'm")
elif yosh >=5 or yosh < 18:
    narh = 10000
    print(f"Chipta {narh} so'm")
else:
    narh = 20000
    print(f"Chipta {narh} so'm")





x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}')
else:
    print(f"{x}>{y}")





mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")





mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")





users = ['alisher1983','aziza','yasina', 'umar']

login = input("Yangi login tanlang: " )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")







"""
Created on Mon Jan 29 00:34:44 2026

# 35 - dars:   Xatolar bilan ishlash

@author: Bahodir
"""



yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except ValueError:
    print("Siz butun sonni kiritmadingiz")
else:
    print(f"Siz {2026-yosh} yilda tug'ilgansiz")

print("Dastur davom etyapti")
print("Dastur tugadi")



#ZeroDivisionError

x, y = 5, 10
try:
    y /(x-5)
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas")




# IndexError


mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
try:
    print(mevalar[5])
except:
    print(f"Ro'yhatda {len(mevalar)} ta meva bor xolos")




# KeyError

user = {"username":"Bahodirdev",
        "status":"admin",
        "email":"admin@bahodirdev",
        "phone":"998999442001"}

key = "tel"
try:
    print(f"Foydalanuvchi: {user[key]}")
except:
    print("Bunday kalit mavjud emas")
    




filename =  "data.txt"   # bunday fayl mavjud emas
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"{filename} mavjud emas")





import json

talaba4 = "Olim Olimov"
talaba = json.dumps(talaba4)
print(talaba)

with open('talaba4.json', 'w') as f:
    json.dump(talaba4, f)





files = ['talaba1.json', 'talaba2.json', 'talaba3.json', 'talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        # print(f"{filename} mavjud emas")
        pass
    else:
        print(talaba)
        # fayl ustida turli amallar




n = input("Butun son kiritiing: ")
try:
    n = int(n)
    x = 20/n
except ValueError: # agar foydalanuvchi butun son kiritmasa
    print("Butun son kiritmadingiz")
except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
    print("0 ga bo'lish mumkin emas")
else:
    print(f"x={x}")



while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
    
print(f"Siz {2026-yosh} yilda tug'ilgansiz")




"""
Created on Mon Jan 29 00:34:44 2026

# 35 - dars:   FILES

@author: Bahodir
"""


file = open('pi.txt')   # bunday usulda faylni o'qish odatda tavsiya berilmaydi

PI = file.read()
print(PI)
file.close()





with open('pi.txt') as files:
    pi = files.read()
    
print(pi)

pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = float(pi)
print(pi)




filename = 'data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)


with open(filename) as file:
    talabalar = file.readlines()
    
print(talabalar)


talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)





faylnomi = 'newfile.txt'
ism = 'Bahodir Ismoilov'
t_yil = 2001
with open(faylnomi, 'w') as fayl:
    fayl.write(ism + '\n')
    fayl.write(str(t_yil) + '\n')





faylnomi = 'newfile.txt'
with open(faylnomi, 'a') as fayl:
    fayl.write('Bositxon Ismoilov\n')
    fayl.write('2004')






import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}


# with open('info', 'wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)







"""
Created on Mon Jan 29 00:34:44 2026

# 35 - dars:   JSon

@author: Bahodir
"""


import json



x = 12
x_json = json.dumps(x)


y = 6.6
y_json = json.dumps(y)


m = True
m_json = json.dumps(m)

sonlar = (6, 12, 50, 64)
sonlar_json = json.dumps(sonlar)





bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

# bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)



# with open('bemor.json', 'w') as f:
#     json.dump(bemor, f)
    

















