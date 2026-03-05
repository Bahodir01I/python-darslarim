# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 19:53:27 2025

14 - dars: DICTIONARY (lug'at)

@author: Bahodir
"""

# 14 - dars: DICTIONARY (lug'at)

# car_0 = {'model': 'ferrari', 'rang': 'qizil' }
# print(car_0['model'])
# print(car_0['rang'])


# en_uz = {'apple': 'olma', 'apricot': "o'rik", 'banana':"banan"}


# mevalar = {'olma': 10000, 'tarvuz':8000, 'qovun':10000}
# print(f"Olma narhi {mevalar['olma']} so'm")



# talaba_0 = {'ism': 'bahodir', 'yosh':24, 't_yil': 2001}
# print(f"{talaba_0['ism'].title()}, {talaba_0['t_yil']}-yilda tug'ilgan, \
#       {talaba_0['yosh']} yoshda")

# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'Artificial Intelligience'
# talaba_0['ism'] = 'Bahodir Ismoilov'


# talaba_1 = {}
# talaba_1['kurs'] = 3
# talaba_1['fakultet'] = 'Matematika'
# talaba_1['ism'] = 'bobir'
# print(talaba_1)
# # print(f"{talaba_1['ism'].title()} {talaba_1['kurs']} kusrsda {talaba_1['fakultet']} yo'nalishida o'qiydi")



# talaba_1['kurs'] = 4
# print(f"{talaba_1['ism'].title()} {talaba_1['kurs']} kusrsda {talaba_1['fakultet']} yo'nalishida o'qiydi")




# talaba_0 = {'ism': 'bahodir', 'yosh':24, 't_yil': 2001}
# del talaba_0['yosh']
# print(talaba_0)


# telefonlar = {
#     'ali':'iphone_7',
#     'vali':'galaxy_9',
#     'bahodir':'iphone_17pro',
#     'olloyor':'iphone_14pro' 
#     }

# phone = telefonlar.get('bahodir')
# print(phone)


#                  """AMALIYOT"""


# 2 mashq

# sevimli_taomlar = {'otam':'osh', 'onam':'manti', 'ukam_1':'somsa', 'ukam_2':"sho'rva", 'ukam_3':"shashlik"}
# print(f"Otamning sevimli ovqati {sevimli_taomlar['otam']}")
# print(f"Onamning sevimli ovqati {sevimli_taomlar['onam']}")
# print(f"Birinchi ukamning sevimli ovqati {sevimli_taomlar['ukam_1']}")
# print(f"Ikkinchi ukamning ovqati {sevimli_taomlar['ukam_2']}")
# print(f"Uchinchi ukamning ovqati {sevimli_taomlar['ukam_3']}")


# 3 mashq

# izohli_lugat = {'integer':'butun son', 'float':'kasr son', 'string':'matn', 
#                 'if':'agar', 'else':'yoki bolmasa', 'variable':'ozgaruvchi', 
#                 'list':'royhat', 'tuple':'ozgarmas royhat', 'dictionary':'lugat', 
#                 'function':'funksoya', 'loop':'takrorlanuvchi'}

# n = input("Iltimos o'rgangan so'zlaringizdan birini kiriting: ").lower()
# print(izohli_lugat.get(n, "Bunday so'z mavjud emas"))



# 4 mashq

# izohli_lugat = {'integer':'butun son', 'float':'kasr son', 'string':'matn', 
#                 'if':'agar', 'else':'yoki bolmasa', 'variable':'ozgaruvchi', 
#                 'list':'royhat', 'tuple':'ozgarmas royhat', 'dictionary':'lugat', 
#                 'function':'funksoya', 'loop':'takrorlanuvchi'}

# n = input("Iltimos o'rgangan so'zlaringizdan birini kiriting: ").lower()
# tarjima = izohli_lugat.get(n)

# if tarjima == None:
#         print('Bunday soz mavjud emas')
# else:
#         print(f"{n.title()} so'zi {tarjima} deb tarjima qilinadi")







#               """ 15 - dars"""

############               LUG'AT BILAN ISHLASH



# talaba_0 = {
#     'ism': 'alijon',
#     'familya':'shamshiyev',
#     'yosh':24,
#     'fakultet':'matematika',
#     'kurs':'4'
#     }


#                            "items()" metodi

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n")




# telefonlar = {
#     'ali':'iphone_7',
#     'vali':'galaxy_9',
#     'bahodir':'iphone_17pro',
#     'olloyor':'iphone_14pro' 
#     }


# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")


#                                "keys()" metodi

# mevalar = {'olma': 10000, 
#             'tarvuz':8000, 
#             'qovun':10000,
#             'anor':20000,
#             'shftoli':11000,
#             'banan':13000}

# print("Do'kondagi mahsulotlar:")
# for mahsulot, narx in mevalar.items():
#     print(mahsulot.title() + ' ' + str( narx))



# print("Do'kondagi mahsulotlar:")
# for mahsulot in mevalar:
#     print(mahsulot.title())


# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mevalar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mevalar[mahsulot]} so'm")
        

# for buyum in bozorlik:
#     if buyum not in mevalar:
#         print(f"Iltimos, do'koningizga {buyum}ni ham olib keling")


# print("Do'koningizda mevalar:")
# for mahsulot in sorted(mevalar):
#     print(mahsulot.title())
    

#                        "vales()" metodi

# print("Foydalanuvhilar quyidagi telefonlarni ishlatishadi: ")
# for tel in telefonlar.values():
#     print(tel)    



# telefonlar = {
#     'ali':'iphone_7',
#     'vali':'galaxy_9',
#     'bahodir':'iphone_17pro',
#     'tohir':'iphone_7',
#     'olloyor':'iphone_14pro',
#     'sobir':'iphone_7',
#     'botir':'iphone_17pro',
#     'hamida':'huawei p30'
#     }

# print("Foydalanuvhilar quyidagi telefonlarni ishlatishadi: ")
# for tel in telefonlar.values():
#     print(tel)


#                              "set()" metodi va set ma'lumot turi

# print("Foydalanuvhilar quyidagi telefonlarni ishlatishadi: ")
# for tel in set(telefonlar.values()):
#     print(tel)


# toys = {"ball", "car", "lamp", "ball", 'bear', 'car'}



                # AMALIYOT
                
# 1 - mashq

# izohli_lugat = {'integer':'butun son', 'float':'kasr son', 'string':'matn', 
#                 'if':'agar', 'else':'yoki bolmasa', 'variable':'ozgaruvchi', 
#                 'list':'royhat', 'tuple':'ozgarmas royhat', 'dictionary':'lugat', 
#                 'function':'funksoya', 'loop':'takrorlanuvchi'}

# for key, value in sorted(izohli_lugat.items()):
#     print(f"{key.title()} - {value}")


# 2 - mashq

# davlatlar = {'uzbekistan':'toshkent', 'roosiya':'moskva', 'us':'washington', 
#              'korea':'seoul', 'yaponiya':'tokio', 'uk':'london','baa':'abu dabi',
#              'turkiya':'istanbul', 'polsha':'varshava', 'germaniya':'berlin'
#              }

# davlat = sorted(davlatlar.keys())
# print(davlat)

# print("Dunyo davlatlari: ")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print("\n O'sha davlatlarning poytaxtlari: ")    
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())


# 3 - mashq

# user = input("Iltimos davlatni kiriting: ")
# for davlat in davlatlar:
#     if davlat in user:
#         print(f"{davlat.title()}ning poytaxti {davlatlar[davlat]}")
#     else:
#         print("Bizda bunday ma'lumot yo'q")


# country = input("Iltimos davlatni kiriting: ")
# capital = davlatlar.get(country)
# if capital == None:
#     print("Bizda bunday ma'lumot yo'q")
# else:
#     print(f"{country.title()}ning poytaxti {capital.upper()}")



# 4 - mashq

# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print("3 ta buyurtmangiz nomini kiriting: ")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom: ").lower())
    

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz bizda bunday {buyurtma} yo'q.")


# print("Iltimos 3 ta buyurtmangiz nomini kiriitng: ")
# buyurtmalar = []
# for i in range(3):
#     buyurtmalar.append(input(f"{i+1}-taom: ").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} - ning narxi-{menu[buyurtma]} so'm")
#     else:
#         print(f"Bizda bunday turdagi {buyurtma} yo'q")




#     16 - dars   NESTING bilan ishlash (Nesting - bu bir narsani ichida boshqa narsani joylash)

# car_0 = {
#     'model': 'lacetti', 
#     'rangi': 'oq',
#     'yili': 2018,
#     'narhi': 13000,
#     'km':50000,
#     'korobka': 'avtomat'
#     }



# car_1 = {
#     'model': 'cobalt', 
#     'rangi': 'qora',
#     'yili': 2015,
#     'narhi': 12000,
#     'km':45000,
#     'korobka': 'mexanika'
#     }


# car_2 = {
#     'model': 'onix', 
#     'rangi': 'oq',
#     'yili': 2024,
#     'narhi': 15000,
#     'km':4600,
#     'korobka': 'avtomat'
#     }

# car = car_0
# print(f"{car['model'].title()}, "
#       f"{car['rangi']} rangli", 
#       f"{car['yili']}-yil, {car['narhi']}$")


# car = car_1
# print(f"{car['model'].title()}, "
#       f"{car['rangi']} rangli", 
#       f"{car['yili']}-yil, {car['narhi']}$")


# car = car_2
# print(f"{car['model'].title()}, "
#       f"{car['rangi']} rangli", 
#       f"{car['yili']}-yil, {car['narhi']}$")


# cars = [car_0, car_1, car_2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rangi']} rangli", 
#           f"{car['yili']}-yil, {car['narhi']}$")



# cars = [car_0, car_1, car_2]
# print(f"{cars[2]['rangi'].title()} "
#       f"{cars[2]['model']}")



# malibus = []
# for i in range(10):
#     new_car = {
#         'model': 'malibu', 
#         'rangi': None,
#         'yili': 2024,
#         'narhi': None,
#         'km':0,
#         'korobka': 'avtomat'
#         }
#     malibus.append(new_car)
    
# for malibu in malibus:
#     print(malibu)


# for malibu in malibus[:3]:
#     malibu['rangi'] = 'qizil'
    
# for malibu in malibus:
#     print(malibu)


# for malibu in malibus[3:6]:
#     malibu['rangi'] = 'qora'
    
    

# for malibu in malibus[6:]:
#     malibu['rangi'] = 'qora'
#     malibu['korobka'] = 'maxanika'
    

# for malibu in malibus:
#     if malibu['korobka'] == 'avtomat':
#         malibu['narhi'] = 40000
#     else:
#         malibu['narhi'] = 35000
        
    
    
# for malibu in malibus:
#     print(malibu)



# dasturchilar = {
#     'ali': ['python', 'c++'],
#     'vali': ['html', 'css', 'js'],
#     'hasan': ['php', 'sql'],
#     'husan': ['python', 'php'],
#     'maryam': ['c++', 'c#']
    
#     }


# # for ism, tillar in dasturchilar.items():
# #     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
# #     for til in tillar:
# #         print(til.upper())
        
        
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()} ", end='')






# hamkasabalar = {
#     'ali':{'familya':'valiyev',
#            't_yil':1995,
#            'malumot':'oliy', 
#            'tillar':['python', 'c++']
#            },
#     'vali':{'familya':'aliyev',
#            't_yil':2000,
#            'malumot':'orta-maxsus', 
#            'tillar':['html', 'c++']
#            },
#     'hasan':{'familya':'husanov',
#            't_yil':1999,
#            'malumot':'maxsus', 
#            'tillar':['php', 'js']
#            },
#     'qodir':{'familya':'holiqov',
#            't_yil':2004,
#            'malumot':'maktab', 
#            'tillar':['java', 'java script']
#            }
#     }

# for ism, info in hamkasabalar.items():
#     print(f"\n{ism.title()} {info['familya'].title()}, "
#           f"{info['t_yil']} - yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           f"Quyidagi dasturlash tilalrini biladi: ")
#     for til in info['tillar']:
#         print(til.upper())
        
        
        
# for ism, info in hamkasabalar.items():
#     print(f"\n{ism.title()} {info['familya'].title()}, "
          # f"{info['t_yil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())        




#   AMALIYOT:
    
# 1 - mashq



# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# navoiy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# qodiriy = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# vohidov = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# shaxlar = [buxoriy, navoiy, qodiriy, vohidov]
# for shaxs in shaxlar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan "
#           f"{vyil-tyil}-yil umr ko'rgan")




# 2 mashq

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)


# 3 - mashq

# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }

# for kalit, lugat in kinolar.items():
#     print(f"\n{kalit.title()} ning sevimli kinolari:")
#     for kino in lugat:
#         print(kino.upper())
    

# 4 - mashq

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }


# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")


# 5 - mashq

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")








