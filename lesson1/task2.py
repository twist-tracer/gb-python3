# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти
# точки.

# диаграмма -> https://drive.google.com/file/d/1humLnGoPjOVVo-ST4AwdSl2Bs7UiBcMC/view?usp=sharing

if __name__ == '__main__':
    x1 = float(input('x1: '))
    y1 = float(input('y1: '))

    x2 = float(input('x2: '))
    y2 = float(input('y2: '))

    if x1 == x2:
        print(f'x = {x1}')
    else:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        print(f'y = {k} * x + {b}')
