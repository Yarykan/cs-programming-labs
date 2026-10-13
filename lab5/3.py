n = int(input())
nije = 0
zero = 0
vihe = 0
for i in range(n):
    f = float(input())
    if f < 0:
        nije += 1
    elif f == 0:
        zero += 1
    else:
        vihe += 1
print("Ниже нуля:", nije)
print("Равны нулю:", zero)
print("Выше нуля:", vihe)
