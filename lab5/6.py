nechet = 0
n = int(input())
for i in range(0,n):
    c = 1
    massive = []
    for k in range(i+1):
        massive.append(c)
        if c % 2 != 0:
            nechet += 1
        c = c * (i - k) // (k + 1)
    print(*massive)
print("Нечетных элементов:", nechet)
        
