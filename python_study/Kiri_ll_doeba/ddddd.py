# pervyi = [int(i) for i in input().split(' ')]
# chetnye = []
# nechetnye = []
# for elementik in pervyi:
#     if elementik % 2 == 0:
#         chetnye.append(elementik)
#     else:
#         nechetnye.append(elementik)
# print(chetnye)
# print(nechetnye)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)
#
# a = int(input())
# while a > 5:
#     a /= 2
#     print(a)

# a = int(input())
# while a < 100:
#     a *= 4
#     print(a)
#     break
# else:
#     print('ne to')
# iteracia = 0
# chisl = int(input())
# chusl = int(input())
# a = chisl + chusl
# if a >= 100:
#     print("bolshe sta")
# else:
#     while a < 100:
#         a += 1
#         iteracia += 1
#     print(iteracia)

# bukvy = ['А','Е', 'Ё', 'И', 'О', 'У', 'Ы',' Э', 'Ю','Я']
# vvod = list(input())
# glas_list = []
# sogl_list = []
# for elem in vvod:
#     if elem in bukvy:
#         glas_list.append(elem)
#     else:
#         sogl_list.append(elem)
# print(glas_list)
# print(sogl_list)


# spisok = [1, 2, 3, 222, 78, 54, 79]  #как работает инсерт#
# spisok.insert(2,89)
# print(spisok)

# spisok = [1, 2, 3, 222, 78, 54, 79]
# pop = spisok.pop(-1)
# print(pop)
# spisok = [1, 2, 3, 222, 78, 54, 79]
# spisok.remove(222)
# print(spisok)
# spisok = [1, 2, 3, 222, 78, 54, 79]
# spisok.index(54)
# print(spisok.index(54))
# spisok = [1, 2, 3, 222, 78, 54, 79, 222, 222]
# spisok.count(222)
#

# spisok = [1, 2, 3, 222, 78, 54, 79, 7, 9]
# spisok.sort()
# print(spisok)

# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#
#     print(i)

# a = int(input())
# b = int(input())
# if a < b:
#      for i in range(a, b + 1):
#          print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(i)

# a = int(input())
# b = int(input())
# c = list(range(b, a + 1))
# d = []
# for item in c:
#     if item % 2 != 0:
#         d.append(item)
# d.sort(reverse=True)
# print(d)


# def do_smth(arg1, arg2, arg3) -> int:
#     print(arg1 + arg2 + arg3)
#
#
# do_smth(1, 2, 3)

# def newfunc(n):
#     def myfunc(x):
#       return x + n
#     return myfunc
# print(newfunc)

# b = int(input())
# a = 2 if b < 100 else 3
# print(a)
# def do_smth():
#     print("WOW")
#
#
# def make_func_do_smth(func):
#     func()
# make_func_do_smth(do_smth)

# (n! или 1*2*3*4*…*n)

# def count_fuckt(arg):
#     if arg == 0:
#         return 1
#     return count_fuckt(arg - 1) * arg
#
#
# print(count_fuckt(4))

# def outer_func(who):
#
# #     def inner_func():
# #         print(f"Hello, {who}")
# #     inner_func()
# #     return(who)
# #
# # print(outer_func("world"))

# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# for i in range(1, 6):
#     print(i, '! = ', factorial(i), sep='')

# # тут ввод с клавиатуры нужных координат для оси x первой клеточки
# x1 = int(input())
#
# # ввод с клавиатуры нужных координат для оси y первой клеточки
# y1 = int(input())
#
# # ввод с клавиатуры нужных координат для оси x второй клеточки
# x2 = int(input())
#
# # ввод с клавиатуры нужных координат для оси y второй клеточки
# y2 = int(input())
#
# # когда ладья ходит, координата по одной из осей не меняется
# # (если не понятно, нарисуйте шахматную доску и подпишите координаты клеточек)
# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')
# # тут ввод с клавиатуры нужных координат для оси x первой клеточки
# x1 = int(input())

# # ввод с клавиатуры нужных координат для оси y первой клеточки
# y1 = int(input())
#
# # ввод с клавиатуры нужных координат для оси x второй клеточки
# x2 = int(input())
#
# # ввод с клавиатуры нужных координат для оси y второй клеточки
# y2 = int(input())
#
# # когда ладья ходит, координата по одной из осей не меняется
# # (если не понятно, нарисуйте шахматную доску и подпишите координаты клеточек)
# if (x1 == x2 + 1 or x1 == x2 or x1 == x2 - 1) and (y1 == y2 + 1 or y1 == y2 or y1 == y2 - 1):
#     print("da")
# else:
#     print("no")
# ход слона
# тут ввод с клавиатуры нужных координат для оси x первой клеточки
# x1 = int(input())
#
# # ввод с клавиатуры нужных координат для оси y первой клеточки
# y1 = int(input())
#
# # ввод с клавиатуры нужных координат для оси x второй клеточки
# x2 = int(input())
#
# # ввод с клавиатуры нужных координат для оси y второй клеточки
# y2 = int(input())
#
# # когда ладья ходит, координата по одной из осей не меняется
# # (если не понятно, нарисуйте шахматную доску и подпишите координаты клеточек)
# # когда ладья ходит, координата по одной из осей не меняется


# sum = 0
# n = 5
# for i in range(1, n + 1):
#     sum += i
# print(sum)

# a = int(input())
# while a != 0:
#     if a < 0:
#         print('Встретилось отрицательное число', a)
#         break
#     a = int(input())
# else:
#     print('Ни одного отрицательного числа не встретилось')

# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1

# def get_raznost(a, b):
#     return a - b
#
#
# def get_summochku(a, b):
#     return a + b
#
# print(get_raznost(get_raznost(50,10),get_summochku(10,10)))

# def printScores(student, *scores):
#    print(f"Student Name: {student}")
#    for score in scores:
#       print(score)
# printScores("Jonathan",100, 95, 88, 92, 99)

# def shit_type(*args, **kwargs):
#     shit_1 = 0
#     shit_2 = 0
#     for i in args:
#         shit_1 += 1
#     print(f"{shit_1} позиционных")
#     for i in kwargs:
#         shit_2 += 1
#     print(f"{shit_2} именных")


# shit_type(1, 2, 4, kwargs=2, kwargs_1=3)

# def get_celoe_chislo():
#     i = 0
#     peremen = input()
#     while i < 3:
#           if peremen.isnumeric():
#               print("Введите число")
#               print(f"{peremen} Инта")
#           i+= 1
#           else:

# def count_max(arg1,arg2):
#     if arg1 > arg2:
#         return arg1
#     else:
#         return arg2
#
# print(count_max(10,15))

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
#     return reversed(bukvy)
# print((reverse_words("1234abcd")))

# def get_fackrorial(arg):
#     if arg == 0:
#         return 1
#     return get_fackrorial(arg - 1) * arg
#
# print(get_fackrorial(4))

def find_number(i):
    if i in range (3,9):
       print("число внутри диапозона")

    else:
        print("числа нет внутри")
    return i
print(find_number(10))
