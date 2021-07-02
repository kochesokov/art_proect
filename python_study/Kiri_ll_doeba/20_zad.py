# def count_max(arg1,arg2,arg3):
#     if arg1 > arg2arg3:
#         return arg1
#     else:
#         return arg2
# #
# print(count_max(3,4,5))

# def get_summa(chisla):
#     all = 0
#     for i in chisla:
#         all += i
#     return all
# print(get_summa((8, 2, 3, 0, 7)))
#
# def count_umnozenia(chisla):
#     all = 1
#     for i in chisla:
#      all *= i
#     return all
# print(count_umnozenia((8, 2, 3, -1, 7)))
# ne sdelano
# def reverse_words(bukvy):
#     list_from_bukvy = list(bukvy)
#     razvorot = list(reversed(list_from_bukvy))
#     opyat_razvorot_blyat = ''.join(razvorot)
#     return opyat_razvorot_blyat
# print((reverse_words('1234abcd')))

# def get_fackrorial(arg):
#     if arg == 0:
#         return 1
#     return get_fackrorial(arg - 1) * arg
#
# print(get_fackrorial(4))

# def find_number(i):
#     if i in range(3, 9):
#         print('число внутри диапозона')
#
#     else:
#         print('числа нет внутри')
#     return i
#
#
# print(find_number(8))
#

#  Напишите функцию Python, которая принимает строку и рассчитывает количество букв верхнего и нижнего регистра.
#  Перейти к редактору
# Пример строки : «Быстрая Лиса Бровей»
# Ожидаемый результат :
# Количество символов в верхнем регистре: 3
# Количество строчных букв: 12

# def string_test(s):
#     d = {'UPPER_CASE': 0, 'LOWER_CASE': 0}
#
#     for c in s:
#         if c.isupper():
#             d['UPPER_CASE'] += 1
#         elif c.islower():
#             d['LOWER_CASE'] += 1
#         else:
#             pass
#     print('Original String : ', s)
#     print('No. of Upper case characters : ', d['UPPER_CASE'])
#     print('No. of Lower case Characters : ', d['LOWER_CASE'])
#
#
# string_test('The quick Brown Fox')
#
# def find_uniqe(arg):
#     s = []
#     for a in arg:
#         if a not in s:
#             s.append(a)
#     return s
# #
#
# print(find_uniqe([1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 55555]))
# Напишите функцию Python, которая принимает число в качестве параметра и проверяет, является ли число простым или нет.
# Примечание. Простое число (или простое число) - это натуральное число, большее 1, которое не имеет положительных
# делителей, кроме 1 и самого себя.

# def find_simple_numb(arg):

# Напишите программу на Python для печати четных чисел из заданного списка. Перейти к редактору
# Список образцов : [1, 2, 3, 4, 5, 6, 7, 8, 9][1, 2, 3, 4, 5, 6, 7, 8, 9]
# Ожидаемый результат : [2, 4, 6, 8]
# def print_chetnye(arg):
#     b = []
#     for a in arg:
#         if a % 2 == 0:
#             b.append(a)
#
#     return b
#
# print(print_chetnye([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# def define_perfect(a):
#     sum = 0
#     for i in range(1, a):
#         if a % i == 0:
#             sum += i
#     return sum == a
# #
# print(define_perfect(29))

# def reverse_words(bukvy):
# #     list_from_bukvy = list(bukvy)
# #     razvorot = list(reversed(list_from_bukvy))
# #     opyat_razvorot_blyat = ''.join(razvorot)
# #     return opyat_razvorot_blyat
# # print((reverse_words('1234abcd')))
# def palindromim_po_polnoy(arg):
#     zavor_v_lst = list(arg)
#     razvor = list(reversed(zavor_v_lst))
#     razvor_bleat = ''.join(razvor)
#     if arg == razvor_bleat:
#         print('Это палиндром')
#     else:
#         print('Не палиндром')
#
#
# palindromim_po_polnoy('kazak')

# def palindromim_2(arg):
#     arg_list = list(arg)
#     while ' ' in arg_list:
#         arg_list.remove(' ')
#     reversev_arg = arg_list[::-1]
#     if reversev_arg == arg_list:
#         print('Это палиндром')
#     else:
#         print('не палиндром')


# palindromim_2('a z b       z          a')

# def palindromim_2(arg):
#     reversev_arg = arg[::-1]
#     zavor_v_liste = list(reversev_arg)
#     listit = list(arg)
#     my_list_spisok = []
#     my_list_2 = []
#     for c in listit:
#         for c in listit:
#             if c != ' ':
#                 my_list_spisok.append(c)
#         for i in zavor_v_liste:
#             if i != ' ':
#                 my_list_2.append(c)
#         if my_list_spisok == my_list_2:
#             print('Это палиндром')
#         else:
# #             print('не палиндром')
# #
#
#
# palindromim_2('Я иду с мечем судия')

# def make_palindrome(arg):
#     arg_list = list(arg)
#     list_without_spaces = []
#     for c in arg_list:
#         if c != ' ':
#             list_without_spaces.append(c)
#     reverse_list_without_spaces = list_without_spaces[::-1]
#     if reverse_list_without_spaces == list_without_spaces:
#         print("Палиндром")
#     else:
#         print("не палиндром")
#
# make_palindrome()

# def find_pangramm(arg):
#     list_with_arg = set(arg)
#     alphabet = (B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z, A, E, I, O, U, Y)
#     for c in alphabet:
#         if c in list_with_arg

class StaticExampleClass:
	static_field = 'I\'M STATIC!'

	def __init__(self):
		self.not_static_field = 'I\'M NOT STATIC!'

	def method_example(self):
		print(self.static_field)
		print(self.not_static_field)

StaticExampleClass().method_example()
