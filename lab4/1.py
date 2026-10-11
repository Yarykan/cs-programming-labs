temp_tek = float(input())
temp_jelat = float(input())
if temp_tek > temp_jelat:
    print('Охлаждение')
elif temp_tek < temp_jelat:
    print('Нагрев')
else:
    print('Выключен')
