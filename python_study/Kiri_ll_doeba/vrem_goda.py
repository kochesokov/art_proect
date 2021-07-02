num_mounth = int(input())
zima = [12, 1, 2]
vesna = [3, 4, 5]
leto = [6, 7, 8]
osen = [9, 10, 11]
if num_mounth in zima:
    print('Зима здесь')
elif num_mounth in vesna:
    print('весна здесь')
elif num_mounth in leto:
    print('лето здесь')
elif num_mounth in osen:
    print('осень здесь')
else:
    print("хуй те")