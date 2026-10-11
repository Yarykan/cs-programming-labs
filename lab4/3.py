x = float(input())
y = float(input())
if y == 0 and x == 0:
    print('Начало координат')
elif y == 0 and x != 0:
    print('Ось X')
elif y != 0 and x == 0:
    print('Ось Y')
elif y > 0 and x > 0:
    print('I четверть')
elif y > 0 and x < 0:
    print('II четверть')
elif y < 0 and x < 0:
    print('III четверть')
elif y < 0 and x > 0:
    print('IV четверть')
