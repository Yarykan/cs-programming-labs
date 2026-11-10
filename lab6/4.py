n = int(input())
summ = 0
count = 0
if n < 0:
    print('Ошибка')
else:
    while n > 0:
        if n % 10:
            c = n % 10
            summ += c
        count += 1
        n = n // 10
print(count, summ)
