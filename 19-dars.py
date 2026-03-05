# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 19:38:11 2025

19 - dars FUNCTIONS (FUNKSIYA)

@author: Bahodir
"""


def salom_ber():
   """Salom beruvchi funksiya"""
   print("Assalomu aleykum!")

salom_ber()


def salom_ber(ism):
    """Foydalanuvchidan ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalomu aleykum, xurmatli {ism.title()}")

salom_ber('Bahodir')
salom_ber('Nodira')


def toliq_ism(ism, familya):
    """Foydalanuvchi ismi va familyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchining ismi: {ism.title()}")
    print(f"Foydalanuvchining familyasi: {familya.title()}")

toliq_ism('Bahodir', 'Ismoilov')



def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchini yoshini hisoblaydigan dastur"""
    print(f"Foydalanuvchining ismi {ism.title()} va u {2025-tugilgan_yil} yoshda")

yosh_hisobla('Bahodir', 2001)



def yoshni_hisobla(tugilgan_yil, joriy_yil=2025):
    """Foydalanuvchidan tugilgan yilini so'rab uni yoshini hisoblaydigan funksiya"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshda siz")

yoshni_hisobla(2001)


#                               AMALIYOT

1 -mashq

def users(ism, yosh):
    """Foydalanuvchini, yoshi, ismi haqida ma'lumot beruvchi funksiya"""
    print(f"Sizning ismingiz {ism.title()}")
    print(f"Siz {2025-yosh} - yilda tug'ilgansiz")

users('Bahodir', 24)


# 2 -mashq

def kub(son):
    """sonning kvadrati va kubini hisoblaydigan funksiya"""
    print(f"Bu {son} sonining kvadrati {son**2} ga teng")
    print(f"Bu {son} sonining kubi {son**3} ga teng")

kub(4)


# 3 - mashq

def toq_son(son):
    """Foydalanuvchi kiritigan sonning toq yoki juftligini aniqlovchi funksiya"""
    if son %2 ==0:
        print(f"Bu kiritgan {son}-soningiz juft son")
    else:
        print(f"Bu kiritgan {son}-soningiz toq son")

toq_son(20)


# 4 - mashq

def katta_son(son_1, son_2):
    """Foydalanuvchi kiritgan ikta sondan kattasini konsolga chiqaradigan funksiya"""
    if son_1 > son_2:
        print(f"bu sonning kattasi {son_1}")
    elif son_2 > son_1:
        print(f"bu sonlardan kattasi {son_2}")
    else:
        print(f"Sonlar o'zaro teng: {son_1 and son_2}")

katta_son(200, 200)


#  5- mashq

def son(x, y):
    """x ning y-chi darajasini chiqaruvchi funksiya"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng")

son(2, 4)




# 6 - mashq

def son(x, y=2):
    """x ning y-chi darajasini chiqaruvchi funksiya"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng")

son(6)


# 7 -  mashq

def son(a):
    """Bu funksiya sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini
    tekshiruvchi funksiya"""
    for i in range(2, 11):
        if a%i==0:
            print(f"Bu {a} soni {i} ga qoldiqsiz bo'linadi ")

son(20)







"""

20 - darr: FUNKSIYADAN QIYMAT QAYTARISH

@author: Bahodir
"""

def toliq_ism_yasa(ism, familya):
    """To'liq ismni qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familya}"
    print(toliq_ism)

toliq_ism_yasa('Bahodir', 'Ismoilov')



def toliq_ism_yasa(ism, familya):
    """To'liq ismni qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familya}"
    return toliq_ism #  bu Local variable deyiladi: yani bu variable funksiyani ichida qolib ketadi

talaba = toliq_ism_yasa('Bahodir', 'Ismoilov')



def toliq_ism_yasa(ism, familya):
    """To'liq ismni qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familya}"
    return toliq_ism

talaba_1 = toliq_ism_yasa('Bobur', 'Abduvohidov')
talaba_2 = toliq_ism_yasa('Islom', 'Latipov')
print(f"Bugun darsga {talaba_1} va {talaba_2}lar keldi")
print(f"Lekin {talaba_1} darsga juda ham kech qolib keldi")



def toliq_ism_yasa(ism, familya, otasining_ismi=''):
    """To'liq ismni qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familya}"
    else:
        toliq_ism = f"{ism} {familya}"
    return toliq_ism.title()

talaba_1 = toliq_ism_yasa('Bahodir', "Ismoilov")
talaba_2 = toliq_ism_yasa('Bositxon', 'Ismoilov', "raximjon ogli")
print(f"Darsga kelgan talabar: {talaba_1} va {talaba_2}")



def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':karobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto_1 = avto_info('GM', 'Malibu', 'Qora', 'avtomat', 2024)
avto_2 = avto_info('GM', 'Trcker', 'Oq', 'Avtomat', 2024, 24500)
avtolar = [avto_1, avto_2]
print("Online bozordagi mavjud avto moshinalar")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'Nomalum'
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")



def oraliq(min, max):
    sonlar =[]
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar

print(oraliq(0, 10))
print(oraliq(10, 21))



def oraliq(min, max, qadam=1):
    sonlar =[]
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar

print(oraliq(0, 10))
print(oraliq(10, 21, 2))




def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

print("Saytimizdagi avtolar ro'yhatini shakllantiramiz")
avtolar = []  # salondagi avtolar uchun bo'sh ro'yhat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting ", end=' ')
    kompaniya = input("\nIshlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narxi: ")

    #Foydalanuvchi kiritgan ma'lumotlarni avto_info yordamida
    #Lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

    #Yana avto qo'shish qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
print("\nSalonimizdagi avtolar: ")
for avto in avtolar:
    if avto['narh']:
        narhi = avto['narh']
    else:
        narhi = 'Nomalum'
    print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narhi}")




#                 AMALIYOT


# 1 va 2 - mashqlar

def mijoz_info(ism, familya, t_yil, manzil, email=None, telefon=None):
    """Mijoz haqida ma'lumotlarni lug'at ko'rinishda qaytaruvchi funksiya """
    mijoz = {'ism':ism,
             'familya':familya,
             'yoshi': 2026-int(t_yil),
             'manzil':manzil,
             'email':email,
             'telefon':telefon}
    return mijoz

print("Mijoz haqidagia ma'lumotlarni kiritamiz")
mijozlar = []

while True:
    print("\nQuyidagi ma'lumotlarni kiriting ", end=' ')
    ism = input("Ismingizni kiriting: ")
    familya = input("Familyangizni kiriting: ")
    t_yil = input("Tug'ilgan yilingizni kiriting: ")
    manzil = input("Yashash manzilingizni kiriting: ")
    email = input("Elektron pochtangizni kiriting: ")
    telefon = input("Telefon raqamingizni kiriting: ")


    mijozlar.append(mijoz_info(ism, familya, t_yil, manzil))

    #Yana davom qo'etishini so'raymiz
    javob = input("Yana malumot qoshasizmi? (ha/yoq) ")
    if javob == 'yoq':
        break

print("Mijozlar ma'lumotlari: ")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familya'].title()}," 
          f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")


# 3 - mashq

def son(x, y, z):
    """Uchta sonni qabul qilib ulardan eng kattasini qaytaruvchi funksiya: """
    max = x
    if y>=max:
        max = y
    if z >=max:
        max = z
    return max
a = son(6, 4, 20)



# 4 - mashq

def aylana(r, pi=3.14):
    """Aylananing radiusini qabul qilib uning diametr, perimetr va yuzini hisoblovchi funksiya"""
    umumiy_m = {"radius":r,
                'diametr':r*2,
                'perimetr':2*pi*r,
                'yuzi':pi*r**2}
    return umumiy_m

s = aylana(6)





"""

21 - darr: FUNKSIYAGA ROYHAT UZATISH 

@author: Bahodir
"""


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()} ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'xasan', 'xusan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)




#             AMALIYOT

# 1 - mashq

def katta_har(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()

ismlar = ['ali', 'vali', 'xasan', 'husan']
katta_har(ismlar)
print(ismlar)


# 2 - mashq

def katta_har(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'xasan', 'husan']
yangi_ism = katta_har(ismlar)
print(ismlar)
print(yangi_ism)


# 3 - mashq

talabalar = ['ali', 'vali', 'xasan', 'xusan']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()} ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar

baholar = bahola(talabalar)
print(baholar)
print(talabalar)








"""

22 - darr: *args va **kwargs

@author: Bahodir
"""


def summa (*sonlar):
    """Kiritilgan sonlarni yig'indisini hiosblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1, 4, 6, 8))
print(summa(1, 40, 60, 800, 87))
print(summa(10, 40, 60, 80, 20, 10))
print(summa(11, 14, 16, 18))
print(summa(12, 43, 64, 85, 96, 100))
print(summa(10000, 20000, 3000, 400, 50, 6))




def summa (x, y, *sonlar):
    """Kiritilgan sonlarni yig'indisini hiosblaydigan funksiya"""
    return x+y+sum(sonlar)

print(summa(1, 4, 6, 8))
print(summa(1, 40, 60, 800, 87))
print(summa(10, 40, 60, 80, 20, 10))
print(summa(11, 14, 16, 18))
print(summa(12, 43, 64, 85, 96, 100))
print(summa(10000, 20000, 3000, 400, 50, 6))
# print(summa(6, y, sonlar))



def avto_info(kompaniya, model, **malumotlar):
    """Avto haqida malumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model'] = model
    return malumotlar

avto_1 = avto_info("GM", "Malibu", rang='qora', yil=2023)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000, korobka='avtomat')



#             AMALIYOT

# 1 - mashq

def istalgan_son(*sonlar):
    """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(istalgan_son(6, 4, 2, 3))



2 - mashq

def talaba(ism, familya, **malumot):
    """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya"""
    malumot['ism']=ism
    malumot['familya'] = familya
    return malumot

student = talaba("Bahodir", 'ismoilov', t_yil=2001, soha='AI')




