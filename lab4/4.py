a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and c+b > a:
    if ((a == b) + (b == c) + (c == a)) == 1:
        print('Равнобедренный')
    elif ((a == b) and (b == c) and (c == a)):
        print('Равносторонний')
    else:
        print('Разносторонний')
else:
    print('Треугольник не существует')
