# Eng katta sonni topish

# a,b,c = input(' 3 son kiriting: ').split()
# a,b,c = int(a),int(b),int(c)

# if a>=b and a>=c:
#     katta = a
# elif b>=a and b>=c:
#     katta = b
# else:
#     katta = c
# print(f'Eng katta son: {katta}')

# 1 dan N gacha yig'indi

# n =10
# s=0
# while n>0:
#     s+=n
#     n-=1
# print(f'sum:{s}')

# Foydalanuvchidan 5 ta son kiritishini so‘rab, ularning o‘rtachasini hisoblang.

# sonlar = [5,8,7,6,3]
# sonlar1 = sonlar.copy()
# s = 0
# while sonlar:
#     s+= sonlar.pop()
# s = s/len(sonlar1)
# print(s)

# Berilgan ro‘yxat ichidan faqat manfiy sonlarni ajratib oling.

# sonlar = [ 5, -8, 3, -2]
# manfiy = []
# for i in sonlar:
#     if i<0:
#         manfiy.append(i)
# print(f'Manfiy sonlar: {manfiy}')

# Foydalanuvchi kiritgan raqamlar kortejga saqlansin va barcha elementlari ekranga chiqarilsin.
# sonlar = []
# print('Sonlar kiriting va yetarli bo\'lganda stop ni kiriting')
# while True:
#     son = input('Son kiriting: ') 
#     if son.lower() != 'stop':
#         sonlar.append(son)
#     else:
#         break
# sonlar = tuple(sonlar)
# print(f'Siz kiritgan sonlar: {sonlar}')

# Talabalar va ularning ballari saqlanadigan dictionary yarating va eng yuqori ball olgan talabani toping.

# talabalar = {
#     'Ali': '80',
#     'Vali': '75',
#     'Anvar': '82',
#     'Salim': '78'
# }
# for key, value in talabalar.items():
#     if value == max(talabalar.values()):
#         print(key)

# Lug‘atda mavjud yoki mavjud emasligini tekshirish. Foydalanuvchi kalit kiritadi, agar mavjud bo‘lsa, qiymatini chiqarish.

# talabalar = {
#     'Ali': '80',
#     'Vali': '75',
#     'Anvar': '82',
#     'Salim': '78'
# }
# ism = 'Salima'
# if ism in talabalar.keys():
#     result = f' {ism} mavjud. Qiymat: {talabalar[ism]}'
# else:
#     result = f'Mavjud emas'
# print(result)

# Foydalanuvchidan satr qabul qilib, uning uzunligini qaytaradigan funksiya yozing.

def uzunlik_top(satr):
    return len(satr)

satr = uzunlik_top('gbhs kjbgr kbgjdv')
print(satr)