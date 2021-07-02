import ast

a = input()
if type(ast.literal_eval(a)) == int:
    print(f'ТЫ написал Int {a}')
else:
    print(f'Ты написал стринг {a}')

