cena = int(input())
age = int(input())
if  0 <= age <= 120:
    if 0 <= age <= 5:
        print(f'Стоимость: {(cena*0):.2f} руб')
    elif 5 <= age <= 17:
        print(f'Стоимость: {(cena*0.5):.2f} руб')
    elif 18 <= age <= 59:
        print(f'Стоимость: {cena:.2f} руб')
    else:
        print(f'Стоимость: {(cena*0.7):.2f} руб')
else:
    print('Ошибка')
