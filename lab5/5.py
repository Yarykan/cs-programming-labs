count = 0
summ = 0
while True:
    stoimost = input()
    if stoimost == 'stop':
        break
    cena = int(stoimost)
    count += 1
    summ += cena
if count == 0:
    print('Нет покупок')
else:
    print("Покупок:", count)
    print("Общая стоимость:", summ, "руб")
    print(f"Средняя стоимость: {summ / count:.2f} руб")
    
