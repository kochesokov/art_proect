# N = int(input())
# M = int(input())
# x = int(input())
# y = int(input())
# if N - x > 0:
#     dx = N - x
#     if N - x > 0:
#         dy = M - y
#     else:
#         dy = N - y
# else: dx = M - x
# if N - x > 0:
#     dy = M - y
# else: dy = N - y
#
# if x <= dx:
#     min = x
# else:
#     min = dx
# if y <= min:
#     min = y
# if dy <= min:
#     min = dy
# print(min)

# 1
# bolshoy_spisok = [int(i) for i in input().split(',')]
# delyatsya_na_dva = [chislo for chislo in bolshoy_spisok if chislo % 2 == 0]
# ne_delyatsa_na_dva = [chislo for chislo in bolshoy_spisok if chislo % 2 == 1]
# print(delyatsya_na_dva, ne_delyatsa_na_dva)


# 2
# spisok = [2, 3, 5, 6, 1, 'mya']
# vtoroy_spisok = [i +1 for i in spisok if type(i) == int]
# print(vtoroy_spisok)

# x = int(input())
# y = int(input())
# while x < y:
#     x +=1
#     print(f'{x} меньше или равен {y}')
# else:
#     x+=1
#     print(f'{x} больше {y}')
#
# A = int(input())
# B = int(input())
# for i in range(A, B+1):
#     if i % 2 == 0:
#         continue
#     print(i)

# 2
# a = input()
# sum = 0
# chisla = []
# while True:
#     if a == 'СТОП':
#         print(f'сумма введенных чисел равна {sum}')
#         break
#     sum += int(a)
#     a = input()

# 3

# chislo = int(input())
# while chislo >= 5:
#     chislo /= 2
#     print(f'{chislo} разделим на 2 получим {chislo}')

# 4

# spisok = [int(a) for a in input().split(',')]
# x = len(spisok)
# index = range(0, x)
# spisok_2 = [spisok[i] for i in index if i % 2 == 1]
# print(spisok_2)

# 5
# spisok = [int(b) for b in input().split(',')]
# x = len(spisok)
# sum = 0
# for i in range(0,x):
#     while sum < 10:
#         sum += spisok[i]
#         print(sum)
#         break
# print(sum)

# 6
# slovo = input()
# glasnaya = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы']
# spisok = [bukva for bukva in slovo if bukva in glasnaya]
# print(spisok)


# 7
flammable_objects = [123, 11, 22, 44, 234, 69]
backend_response = {
   'result': [
       {
           'post_number': 123352,
           'post_date': '2019-12-11',
           'package_items_ids': [
               1235,
               234,
               1234,
               432,
               15,
               11,
               2
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 2100,
           'flammable': False,
           'status': 'arrived'
       },
       {
           'post_number': 12345,
           'post_date': '2019-12-11',
           'package_items_ids': [
               1235,
               1111,
               1234,
               432,
               15,
               2
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 2100,
           'flammable': True,
           'status': 'arrived'
       },
       {
           'post_number': 43242,
           'post_date': '2019-12-11',
           'package_items_ids': [
               23,
               13,
               22,
               432,
               44,
               235,
               2
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 2000,
           'flammable': False,
           'status': 'arrived'
       },
       {
           'post_number': 11125,
           'post_date': '2019-12-11',
           'package_items_ids': [
               43,
               11111,
               2,
               11,
               555,
               44,
               10
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 3100,
           'flammable': True,
           'status': 'arrived'
       },
       {
           'post_number': 432423,
           'post_date': '2019-12-11',
           'package_items_ids': [
               324,
               532,
               3333,
               2345,
               22,
               115,
               2
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 1150,
           'flammable': True,
           'status': 'arrived'
       },
       {
           'post_number': 32532,
           'post_date': '2019-12-11',
           'package_items_ids': [
               5436,
               7645,
               456,
               5357,
               34,
               54,
               3
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 2100,
           'flammable': False,
           'status': 'arrived'
       },
       {
           'post_number': 2323,
           'post_date': '2019-12-11',
           'package_items_ids': [
               432,
               5435,
               6546,
               76,
               45,
               34,
               3
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 1201,
           'flammable': True,
           'status': 'arrived'
       },
       {
           'post_number': 1111,
           'post_date': '2019-12-11',
           'package_items_ids': [
               654,
               345,
               44,
               765,
               9,
               5,
               1
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 1100,
           'flammable': False,
           'status': 'arrived'
       },
       {
           'post_number': 576734,
           'post_date': '2019-12-11',
           'package_items_ids': [
               546,
               1111,
               645,
               754,
               22,
               765,
               54
           ],
           'city': 'Moscow',
           'country': 'Russia',
           'weight': 1234,
           'flammable': True,
           'status': 'arrived'
       }
   ]
}
# s = 0
# korrektno = []
# # flame_true = [posylka for posylka in backend_response['result'] if posylka['flammable'] == True]
# posylka = backend_response['result']
# for t in range(0, len(posylka)):
#     # print(posylka[t])
#     element = posylka[t]
#     paket = element['package_items_ids']
#     # print(paket)
# for s in range(0, len(flammable_objects)):
#     em = flammable_objects[s]
#     if em in paket:
#         korr = korrektno.append(paket)
#     print(korrektno)
# x = len(flame_true)
# for i in range(0, x):
#     nomera_7 = flame_true[i]
#     h = nomera_7.get('package_items_ids')
#     print(h)
# print(element)

# k = 0
# flame = flammable_objects[k]
# pakety = backend_response['result']
# prishli = []
#
# for n in range(0,8):
#     a = pakety[n]
#     nomera_paketov = a.get('package_items_ids')
# g = list(nomera_paketov)
# g = pakety[5].get('package_items_ids')
# if flame in g:
#         korsina = prishli.append(nomera_paketov)
#         k +=1
#         print(prishli)


# 8
# legkie_posylki = [posylka for posylka in backend_response['result'] if posylka['weight'] < 2000]
# n = 0
# while n < len(legkie_posylki):
#     nomera_8 = legkie_posylki[n]
#     print(nomera_8.get('post_number'))
#     n += 1


# 9
# korrektno_i_legko = [posylka for posylka in backend_response['result'] if posylka['flammable'] == False or posylka['weight'] >= 2000]
# x = len(korrektno_i_legko)
# for i in range(0, x):
#     nomera_9 = korrektno_i_legko[i]
#     h = nomera_9.get('post_number')
#
#     print(h)
# print(f'количество некорректных посылок: {len(korrektno_i_legko)}')
posylky = backend_response()