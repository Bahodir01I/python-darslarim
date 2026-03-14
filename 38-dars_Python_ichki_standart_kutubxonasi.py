"""
Created on Sat Jan 31 00:30:27 2026

#38-dars. PYTHON KUTUBXONASI


@author: Bahodir
"""

import datetime as dt  ## date() moduli vaqtlar va sanalar bilan ishlash u-n kerak bo'ladi

hozir = dt.datetime.now()
print(hozir)

# # sanani ajratib olish
print(hozir.date())

## vaqtni ajratib olish
print(hozir.time())

## soatni ajratib olish
print(hozir.hour)

## minutni ajratib olish
print(hozir.minute)


## secundni ajratib olish
print(hozir.second)





# date() bu faqat sanani chiqaradi

bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")
ertaga = dt.date(2026, 2, 1)
print(f"Ertangi sana: {ertaga}")





# time() faqat vaqtni chiqarish uchun time() metodini ishlatamiz

hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")
vaqtKeyin = dt.time(2, 20, 44)
print(vaqtKeyin)




##  Sanalar orasidagi farq

bugun = dt.date.today()
ramazon = dt.date(2026, 2, 18)
farq = ramazon - bugun
print(f"Ramazonga {farq.days} kun qoldi")



##  Soatlar orasidagi farq

bugun = dt.datetime.now()
futbol = dt.datetime(2026, 2, 14, 23, 50, 0)
farq = futbol - bugun
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {farq.days} kuni {soatlar} soat qoldi")





import math  # math moduli matematika oid amallarni bajarish uchun ishlatiladi


PI = math.pi
print(f"PI ning qiymati: {PI}")
E = math.e
print(f"e ning qiymati: {E}")



# trigonometriya

a = math.sin(math.pi/2)
b = math.cos(0)
c = math.tan(PI)


# radianlar va burchaklar o'rtasidagi konvertatsiya
print(math.degrees(math.pi/2))
print(math.radians(90))



# logarifmlar
# natural
math.log(5)
# 10 asosli logarifm
math.log10(100)



# sonlarni yaxlitlash#

x = 6.6
print(math.ceil(x))
print(math.floor(x))




# # Kvadrat ildiz

x = 81
math.sqrt(x)


# # Darajaga oshirish
math.pow(x, 3)  # x ning kubi
math.pow(x, 5)  # s ning 5-darajasi
math.pow(x, 1/3) # x dan kub ildiz






from pprint import pprint   #  pprint bu chiroyli modul degani
import json


filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    

print(bemor)
pprint(bemor)


# import requests  # bu tashqi modul
#
# r = requests.get('https://api.github.com')
#
# print(r.json())
# pprint(r.json())





#       RegEx  -  Regular Expressions - andozlar, bu matnlarni izlash uchun andozlar yaratishda ishlatiladi bu modul


import re
from uzwords import words



word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))


andoza = "^т...р$"
matches = []

for word in words:
    if re.match(andoza, word):
        matches.append(word)
        
print(matches)





# Emailni ajratib olish

matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)




# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi

andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")



#                       AMALIYOT

# 1 - mashq


import datetime as dt


d = dt.date.today()

for i in range(10):
    print(d)
    d +=dt.timedelta(weeks=2)
    

# 2 - mashq

today = dt.date.today()
ramazon = dt.date(2026, 2, 18)
farq = ramazon - today
print(f"Ramazongacha {farq} kun qoldi")


# 3 mashq

today = dt.date.today()
t_yil = dt.date(2001, 4, 20)
yil = today.year - t_yil.year
month = t_yil.month - today.month
kun = today.day - t_yil.day
print(f"Tug'ilgan kunimdan boshlab, hozirgi kungacha {yil} yil, {month} oy va {kun} kun o'tdi")



# 4 - mashq

import re

andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

msg = "Teleon nomeringizni kiriting: "
msg += '(kamida 8 raqamdan iborat bo\'lishi, yani kodi bilan kiriting): '


while True:
    phone = input(msg)
    if re.match(andoza,phone):
        print("Telefon raqamingiz mos keldi")
        break
    else:
        print("Bunday telefon raqam mavjud emas!")





# 5 - masala

import re

msg = ('Assalom alaykum hurmatli do\'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI '
       'Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur '
       'yozishni o\'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test')

andoza = r"https?://[^\s]+"

veb = re.findall(andoza, msg)
print(veb)















