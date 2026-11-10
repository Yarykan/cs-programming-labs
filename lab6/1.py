a = int(input())
b = int(input())
if a <= 0 or b <= 0:
    print('Ошибка')
else:
    while b > 0:
        c = a % b
        a = b
        b = c
    print(f'НОД: {a}')
    
