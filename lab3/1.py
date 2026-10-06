kod_format = str(input())
razdel = kod_format.split('-')
nomer = razdel[2]
print(f'Категория: {razdel[0]}')
print(f'Год: {razdel[1]}')
print(f'Номер: {nomer}')
print(f'Обратный номер: {nomer[::-1]}')
