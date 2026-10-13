a = int(input())
b= int(input())
summ = 0
proizved = 1
for i in range(a,b+1):
    summ += i
    proizved *= i
print("Сумма:", summ)
print("Произведение:", proizved)
